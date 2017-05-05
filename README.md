# EasyPeasey
Metasploit/MSFVenom Payload Generator Stand Alone

# New Video of How to use Encoder Tester Mode here: http://www.dailymotion.com/video/x5kelz9

## EasyPeasey takes the frustration and uncertainty of typing console commands out of your hands
Newest version of EasyPeasey can be run as a Terminal Command:

> EZPZ.py

Be sure to update your git repos or simply follow the new installation instructions below (fully automatic, requires python)

# Features

As of March 26th, 2017, incorporates payloads available on Metasploit, including but not limited to...
    Windows
    Mac OSX
    Android
    Linux
    Java
    Ruby

# Update, New Installation Method, Python-AutoInstaller

Due to some weird bug where git cloning does not pull the latest version, I had to use a python auto-installer script to make it work. 
This python script will automatically perform the correct settings to keep the git submodules updated and pull the latest version.

Following the following steps, from terminal:

>cd /tmp

>git clone https://github.com/tanc7/EasyPeasey

>cd EasyPeasey

>python setup_Easy_Peasey.py

Then go grab a coffee. 

# BUG ALERT, FIX ON THE WAY
The dev has recently discovered several bugs in the program.

        1. Android payloads that have been encoded cannot be installed "parse error"
        2. Some payloads may not work just because its encoded
        3. Windows payloads STILL WORK perfectly if it evades antivirus
        4. For Android and Python payloads, the only format specification should be "raw".
        5. Python payloads also cannot be encoded, "syntax error" on execution by victim.

The dev is working on it right now. He will

        1. First commit the changes to the ArmsCommander Repo after extensive testing
        2. And then quickly fork it over to the Stand-Alone Easy-Peasey Repo which should only take minutes
        3. The dev is also going to change the encoder-tester module. It will now be able to generate working payloads in its own directory.
        4. As well as changing the setup file to create the proper tester payload folder for it to work
    
Status

        1. Python and Android payloads are fixed in tester version. No encoding will be accepted, otherwise it wont work.
        2. Mac format is changed to ".macho". Cannot be tested unless one of you happens to have a Mac OS X image I can use in a VM
        3. The Encoder-Tester App is now changed to generate one of each payload and will ask you to provide a LHOST and LPORT, so that you can test them yourself before launching them.
        4. Linux payloads do not appear to be working at all. Neither as a non-encoded ELF file, or encoded. Chmodding them to 777 does nothing. 
        5. It is RECOMMENDED to instead launch Python payloads instead against both Linux and Mac targets. Both of them as well as other *nix type OSes can execute Python natively.
        6. Ruby might also require no-encoding
            a. Confirmed. Ruby Command Shell opens only without any encoding. However, not recommended to be used
            >[*] XX.XXX.XXX.XXX - Command shell session 1 closed.  Reason: Died from EOFError
        7. Java payloads CAN BE ENCODED and EXECUTED "java -jar file.jar"
        8. 2:54am PST, initial patch is being developed

        
