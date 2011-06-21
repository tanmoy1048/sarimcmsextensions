#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       flasuck.py
#
#       Copyright 2011 Sarim Khan <sarim2005@gmail.com>
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

__author__ = 'sarim khan'
import subprocess,re,os,random,string,sys


c = 0

def getrandname():
    global c
    c = c + 1
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6)) + '_' + str(c)
def bcktik(cmd):
    p = subprocess.Popen(['/bin/sh', '-c', cmd],stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()
def copytod(source,desti):
    return bcktik('cat \'' + source + '\' > \'' + desti + '\'')

try:
    tgdir = sys.argv[1].strip()
    if tgdir == 'help' or tgdir == '-help' or tgdir == '--help' or tgdir == '-h':
        print '''usage: flasuck [option] [DestDir]
Options and arguments :

-h
--help
--help
help         : Show this help screen and exit

DestDir      : Write file into DestDir, must be a valid directory. Will select `pwd` when not provided'''
        os._exit(0)
except:
    tgdir = bcktik('pwd').strip()

if os.uname()[0] == 'Darwin':
    print 'Darwin kernel detected :) \nScan Started'
    s = bcktik('lsof | grep Flash')
    m = re.findall('\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(.+)', s)
    for ss in m:
        fst = bcktik('file \'' + str(ss) + '\'')
        if ('Flash Video' in fst ):
            dess = tgdir + '/' + getrandname() + '.flv'
            print 'copying to => ' + dess + ' :) \n'
            print copytod(ss,dess)
elif os.uname()[0] == 'Linux':
    print 'Linux kernel detected :) \nScan Started'
    s = bcktik('lsof | grep Flash')
    m = re.findall('\S+\s+(\S+)\s+.+', s)
    pidd = str(m[0]).strip()
    ss = bcktik('file /proc/' + pidd + '/fd/* | grep Flash')
    mm = re.findall('(.+)[:].+', ss)
    for ss in mm:
        dess = tgdir + '/' + getrandname() + '.flv'
        print 'copying to => ' + dess + ' :) \n'
        print copytod(ss,dess)

else:
    print 'Unsupported OS. only Linux and Darwin kernels are supported now.'

print "Finished Copying " + str(c) + " File(s)\nflasuck.py - Flash Media Sucker (c) 2011 by Sarim Khan "
