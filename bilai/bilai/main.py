#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       bilai.py
#       
#       Copyright 2010 Sarim Khan <sarim2005@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import urllib2,urllib,shelve, sys
from BeautifulSoup import BeautifulSoup as BTS , Tag
from os import environ
from PyQt4.QtGui import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QWidget
from PyQt4.QtCore import pyqtSignature, QThread, SIGNAL
from Ui_bilai_form import Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.tableWidget.hide()
        self.sts_lb.hide()
        self.sts_pb.hide()
        self.thd = fetchdata(self)
        self.connect(self.thd, SIGNAL("finished()"), self.updateUi)
        self.connect(self.thd, SIGNAL("terminated()"), self.updateUi)
        self.connect(self.thd, SIGNAL("started()"), self.startUi)

        try:
            
            db = shelve.open(environ['HOME'] + "/.blnset.conf", 'r')
            self.txtUser.setText(db['username'])
            self.txtPass.setText(db['password'])
            self.txtFrom.setText(db['StartDate'])
            self.txtTo.setText(db['EndDate'])
            self.checkBox.setChecked(bool(db['checkb']))
            db.close()
        except:
            print 'could not read from setting, maybe first time ?'
    def updateUi(self):
        self.tableWidget.show()
        self.sts_lb.hide()
        self.sts_pb.hide()
    def startUi(self):
        self.tableWidget.hide()
        self.sts_lb.show()
        self.sts_pb.show()
        self.tabWidget.setCurrentIndex(1)
    def save_st(self):
        try:
            db = shelve.open(environ['HOME'] + "/.blnset.conf", 'n')
            db['username'] = str(self.txtUser.text()).strip()
            db['password'] = str(self.txtPass.text()).strip()
            db['StartDate'] = str(self.txtFrom.text()).strip()
            db['EndDate'] = str(self.txtTo.text()).strip()
            db['checkb'] = int(self.checkBox.isChecked())
            db.close()
        except:
            print 'could not write setting'
    def sh_abt(self):
        abtbox = QMessageBox(self)
        abtbox.setText('This app is for BanglaLion users. Just click the buttons and you will know about it by yourself ;)\n\nCreated By Sarim Khan\n\nsarim2005@gmail.com')
        abtbox.setWindowTitle('About')
        abtbox.show()
    def show_err(self, msg):
        abtbox = QMessageBox(self) 
        abtbox.setText(msg)
        abtbox.setWindowTitle('Error')
        abtbox.show()
    def show_u(self):
        self.thd.begin()
    def showtable(self):
        try:
            
            self.sts_lb.setText('Fetching Data , Please wait ........')
            self.sts_pb.setValue(1)
            
            theurl = 'https://care.banglalionwimax.com/User'
            username = str(self.txtUser.text()).strip()
            password = str(self.txtPass.text()).strip()
            StartDate = str(self.txtFrom.text()).strip()
            EndDate = str(self.txtTo.text()).strip()
            if self.checkBox.isChecked() :
                self.save_st()
            values = {"Page":"UsrSesHit","Title":"Session Calls","UserID":username,"StartDate":StartDate,"EndDate":EndDate,"Submit":"Submit"}
            
            data = urllib.urlencode(values)
            req = urllib2.Request(theurl, data)
            self.sts_pb.setValue(2)


            passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
            # this creates a password manager
            passman.add_password(None, theurl, username, password)
            # because we have put None at the start it will always
            # use this username/password combination for  urls
            # for which `theurl` is a super-url

            authhandler = urllib2.HTTPBasicAuthHandler(passman)
            # create the AuthHandler

            opener = urllib2.build_opener(authhandler)
            self.sts_pb.setValue(3)
            urllib2.install_opener(opener)
            # All calls to urllib2.urlopen will now use our handler
            # Make sure not to include the protocol in with the URL, or
            # HTTPPasswordMgrWithDefaultRealm will be very confused.
            # You must (of course) use it when fetching the page though.
            
            self.tableWidget.clear()
            pagehandle = urllib2.urlopen(req)
            # authentication is now handled automatically for us
            self.sts_pb.setValue(4)
            ht = pagehandle.read()
            
            soup = BTS(ht, convertEntities=BTS.HTML_ENTITIES)
            table =  soup.findAll('table')[14]        
            rows = table('tr')
            rowcount = rows.__len__()
            self.tableWidget.setRowCount(rowcount-1)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['MAC ID', "DATE", "FROM" ,  'KB' ,  'MB' ,  'GB'])
            self.usage = 0
            for rx in range(1, rowcount-1):
                cols = rows[rx]('td')
                colcount = cols.__len__()
                if rx == ( rowcount-2):
                    itemm = QTableWidgetItem(str("%.2f" % (float(self.usage) / 1024) ))
                    itemg = QTableWidgetItem(str("%.2f" % (float(self.usage) / 1048576) ))
                    self.tableWidget.setItem(rx, 4, itemm)
                    self.tableWidget.setItem(rx, 5, itemg)
                    item = QTableWidgetItem(str(self.usage))
                    self.tableWidget.setItem(rx, 3, item)
                    itemt = QTableWidgetItem('Total')
                    self.tableWidget.setItem(rx, 2, itemt) 
                for cx in range(1, colcount):
                    col = cols[cx].text
                    if cx == 4:
                        self.usage = self.usage + int(col)
                        imb = float(col) / 1024
                        igb = imb / 1024
                        itemm = QTableWidgetItem(str("%.2f" % imb))
                        itemg = QTableWidgetItem(str("%.2f" % igb))
                        self.tableWidget.setItem(rx-1, 4, itemm)
                        self.tableWidget.setItem(rx-1, 5, itemg)
                    item = QTableWidgetItem(col)
                    self.tableWidget.setItem(rx-1, cx-1, item)
            self.sts_pb.setValue(5)
            
        except:
            self.sts_lb.setText( "Error :" + (str(sys.exc_info()[1])))
            
        
    
class fetchdata(QThread): 
    def __init__(self, guis): 
        QThread.__init__(self, guis) 
        self.guis = guis
        

    def run(self): 
        self.guis.showtable()
            
        
    def begin(self): 
        self.start()
        
if __name__ == "__main__":



    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
