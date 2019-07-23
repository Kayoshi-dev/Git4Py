#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Simple Python 3 script to interact with a Github repository

import subprocess, os, glob, io

urlRepo = "https://github.com/Kayoshi-dev/SimpleOOPDashboard"
dirname = urlRepo.split('/')[4]

def gitMain():
    print("""

    Welcome to :
       ______   _   _    _    _    _______         
     .' ___  | (_) / |_ | |  | |  |_   __ \        
    / .'   \_| __ `| |-'| |__| |_   | |__) |_   __ 
    | |   ____[  | | |  |____   _|  |  ___/[ \ [  ]
    \ `.___]  || | | |,     _| |_  _| |_    \ '/ / 
     `._____.'[___]\__/    |_____||_____| [\_:  /  
                                           \__.'   
    """)

    gitClone()

#This function clone a repository
def gitClone():
    if os.path.exists(os.getcwd() + os.sep + dirname):
        os.chdir(dirname)
        try:
            pullResult = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
            print('Updating...⌛')
            while True:
                line = pullResult.stdout.readline()
                if not line:
                    break
                print(line)
        except subprocess.CalledProcessError as e:
            print('❌ An error has occurred : ', e.returncode)
    else:
        try:
            cloneResult = subprocess.Popen(['git', 'clone', urlRepo], stdout=subprocess.PIPE)
            print('Downloading the Github repository...⌛')
            while True:
                line = cloneResult.stdout.readline()
                if not line:
                    break
                print(line)
            print('Finished!💪')
        except subprocess.CalledProcessError as e:
            print('❌ An error has occurred : ', e.returncode)

gitMain()