#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


transport_Dict = {
    '1': 'obfs3',
    '2': 'udp',
    '3': 'http',
    '4': 'tcp_cleartext',
    '5': 'rsa',
    '6': 'ssl',
    '7': 'udp_cleartext',
    '8': 'scramblesuit',
    '9': 'ssl_rsa'
}

# change directory to pupysh server
os.chdir('/root/pupy/pupy')

# port 443 for ssl encoding and so on
os.system('sudo python /root/pupy/pupy/pupysh.py -t ssl -p 443')
os.system('sudo python /root/pupy/pupy/pupysh.py -t udp -p 1111')
os.system('sudo python /root/pupy/pupy/pupysh.py -t http -p 2222')
os.system('sudo python /root/pupy/pupy/pupysh.py -t tcp_cleartext -p 3333')
os.system('sudo python /root/pupy/pupy/pupysh.py -t rsa -p 4444')
os.system('sudo python /root/pupy/pupy/pupysh.py -t udp_cleartext -p 5555')
os.system('sudo python /root/pupy/pupy/pupysh.py -t scramblesuit -p 7070')
os.system('sudo python /root/pupy/pupy/pupysh.py -t sslrsa -p 8080')
os.system('sudo python /root/pupy/pupy/pupysh.py -t obfs3 -p 10000')
