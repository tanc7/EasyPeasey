import os
import socket
import operator
from termcolor import colored

os.system('service postgresql start')
os.system('service metasploit start')
os.system('msfdb init')
os.system('msfdb start')
os.system('msfconsole')
os.system('db_status')
