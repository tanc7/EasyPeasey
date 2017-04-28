# EasyPeasey
Metasploit/MSFVenom Payload Generator Stand Alone

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

> git submodule init

> git submodule update

>python setup_Easy_Peasey.py

Then go grab a coffee. 

# New Feature: Test all 39 Metasploit encoders against a single payload type
Video Explaining this process and how-to-use here:
http://www.dailymotion.com/video/x5k2hcc (link changed due to Copyright issues with the music track)

Purpose:

        1. Helps you quickly decide which encoders is best to use based on...
        2. Whether the encoding went smoothly
        3. Overall filesize of the output payload
        4. Minimalist in disk space (it overwrites itself 39 times basically).
 
