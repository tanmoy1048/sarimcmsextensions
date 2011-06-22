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

import urllib, sys
from BeautifulSoup import BeautifulSoup as BTS , Tag
from os import environ
from PyQt4.QtGui import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QWidget
from PyQt4.QtCore import pyqtSignature, QString, QUrl, QByteArray, QSettings
from PyQt4.QtNetwork import QNetworkRequest, QNetworkAccessManager
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
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.replyFinished)
        self.manager.sslErrors.connect(self.n_error)
        self.settings = QSettings('SarimKhan','BLionUsageV')
        
        try:
            
            self.txtUser.setText(str(self.settings.value('username').toString()))
            self.txtPass.setText(str(self.settings.value('password','123456').toString()))
            self.txtFrom.setText(str(self.settings.value('StartDate').toString()))
            self.txtTo.setText(str(self.settings.value('EndDate').toString()))
            self.checkBox.setChecked(bool(self.settings.value('checkb',True).toBool()))
            
        except:
            print (str(sys.exc_info()[1]))

    def save_st(self):
        try:
            self.settings.setValue('username', str(self.txtUser.text()).strip())
            self.settings.setValue('password' ,  str(self.txtPass.text()).strip())
            self.settings.setValue('StartDate' ,  str(self.txtFrom.text()).strip())
            self.settings.setValue('EndDate' ,  str(self.txtTo.text()).strip())
            self.settings.setValue('checkb' ,  int(self.checkBox.isChecked()))
        except:
            print 'could not write setting'
    def sh_abt(self):
        abtbox = QMessageBox(self)
        abtbox.setText('This app is for BanglaLion users. Just click the buttons and you will know about it by yourself ;)\n\nCreated By Sarim Khan\n\nsarim2005@gmail.com')
        abtbox.setWindowTitle('About')
        abtbox.show()

    def replyFinished(self, reply):
        try:
            if (int(reply.error())) <> 0:
                raise NameError(reply.errorString())
            ht = reply.readAll()
            soup = BTS(str(ht), convertEntities=BTS.HTML_ENTITIES)
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
                    self.tableWidget.show()
                    self.sts_lb.hide()
                    self.sts_pb.hide()
        except:
            self.sts_lb.setText( "Error :" + (str(sys.exc_info()[1])))


    def n_error(self, reply, errs):
        reply.ignoreSslErrors()
        for er in errs:
            print ("Error Code : %s\nError : %s" % (er.error(), er.errorString()))
    def dwn(self, r, t):
        self.sts_pb.setValue(r)
    def show_u(self):
        try:
            self.tableWidget.hide()
            self.sts_lb.show()
            self.sts_pb.show()
            self.sts_lb.setText('Fetching Data , Please wait ........')
            self.sts_pb.setValue(1)
            self.tabWidget.setCurrentIndex(1)
            theurl = 'https://care.banglalionwimax.com/User'
            username = str(self.txtUser.text()).strip()
            password = str(self.txtPass.text()).strip()
            StartDate = str(self.txtFrom.text()).strip()
            EndDate = str(self.txtTo.text()).strip()
            if self.checkBox.isChecked() :
                self.save_st()
            values = {"Page":"UsrSesHit","Title":"Session Calls","UserID":username,"StartDate":StartDate,"EndDate":EndDate,"Submit":"Submit"}
            
            data = urllib.urlencode(values)
            nr = QNetworkRequest(QUrl("https://care.banglalionwimax.com/User"))
            nr.setRawHeader("Authorization", QString("Basic " + QByteArray(QString("%s:%s" %(username,password)).toLocal8Bit().toBase64())).toLocal8Bit())
            dat = QByteArray()
            dat.append(data)
            rp = self.manager.post(nr,dat)
            rp.downloadProgress.connect(self.dwn)
            self.tableWidget.clear()


            
        except:
            self.sts_lb.setText( "Error :" + (str(sys.exc_info()[1])))
            
        
    
        
if __name__ == "__main__":



    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
