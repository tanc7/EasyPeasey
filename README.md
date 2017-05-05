# EasyPeasey
Metasploit/MSFVenom Payload Generator Stand Alone Version (forked from ArmsCommander)

1. Rapidly generate payloads in seven different file formats and operating system executables.
2. Automatically generates for you, a easy resource-file startup script for Metasploit (.rc file)
3. Automatically adds stage-encoding whenever possible
4. Test encoder effectiveness for specific payload types on the fly
5. Has incorporated all of the remote-exploits section from the ArmsCommander.

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

# BUG FIXES, May 5th

The dev has made the following changes to fix several bugs for EasyPeasey

	1. Eliminated encoder options for Python, Ruby, and Android payloads because they do not execute properly ('syntax error', 'parse error', etc.)
	2. The generator automatically adds the correct file extension type to the payload (you do not need to add a file extension)
	3. Renumbered the list of encoders (for some reason the numbers disappeared from the text file before)
	4. The Linux Metasploit payload appears to not be working in ANY shape or form, neither encoded or not
	5. Mac payload cannot be tested unless I can acquire a VM image.
	6. Recommends either Python or Java payloads to target Linux, Unix, and Mac machines

Here is a list of which payloads can be encoded:

	1. Windows - YES
	2. Mac - Unknown
	3. Linux - Unknown
	4. Python - NO
	5. Ruby - NO & appears to be buggy
	6. Java - YES
	7. Android - NO

    

