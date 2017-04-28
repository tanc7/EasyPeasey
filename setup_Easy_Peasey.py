#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable
import os
import socket


# git clone
print '[+] Git cloning latest GitHub Release'
tmp_dir = '/tmp'
os.chdir(tmp_dir)
cmd_String = 'git clone https://github.com/tanc7/EasyPeasey'
os.system(cmd_String)
print '[+] Creating directories'
curr_EZPZ_dir = './EasyPeasey'
os.chdir(curr_EZPZ_dir)
os.system('mkdir /root/EZPZ/')
print '[+] Copying files'

os.system('chmod 777 ./*')
os.system('cp -r ./* /root/EZPZ')
os.system('cp -r EZPZ.py /usr/local/bin')


print '[+] Installing Python Package prerequisites'

cmd_String = "pip install -r /root/ArmsCommander/remoteexploits/EZPZ_Requirements.txt"
os.system(cmd_String)

print '[+] Updating your Metasploit Framework Installation'
os.system('msfupdate')

print '[+] Done. You should be able to access EasyPeasey by going to the console and typing:'
print 'EZPZ.py'

print '[+] Launching EasyPeasey as a terminal command.'
cmd_String = 'EZPZ.py'
os.system(cmd_String)
