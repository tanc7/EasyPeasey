#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
# from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

def installer():
    # git clone
    try:
        print '[+] Git Cloning to /root'
        gc_URL = 'https://github.com/nathanlopez/Stitch'
        install_dir = '/root'
        stitch_dir = '/root/Stitch'
        os.chdir(install_dir)
        os.system('git clone ' + gc_URL)
        os.chdir(stitch_dir)
        os.system('git submodule init')
        os.system('git submodule update')
        # install from requirements
        print '[+] Installing Linux Requirements'
        os.system('pip install -r /root/Stitch/lnx_requirements.txt')

        # install replacement to PIL (which has been deprecated)
        print '[+] Installing Pillow which is the replacement to PIL(deprecated)'
        os.system('pip install pillow')

        print '[+] Installation Completed'
        print '[*] Test running Stitch'
        os.system('python /root/Stitch/main.py')

    except (TypeError, NameError):
        print '[-] An error is thrown'
        print '[-] There must be a bug or typo in this program, please notify the dev'
        print TypeError
        print NameError
        main()
    except (RuntimeError):
        print '[-] An error is thrown'
        print '[-] A runtime is not installed'
        print RuntimeError
    except KeyboardInterrupt:
        print '[-] Received CTRL+C, quitting'

def main():
    continue_install = str(raw_input("Type INSTALL to continue (Yes again...): "))
    if continue_install == "INSTALL":
        installer()
        main()
    else:
        print 'Type INSTALL and hit [Enter] please...'
        main()
main()
