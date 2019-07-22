#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Simple Python 3 script to interact with a Github repository

import subprocess

urlRepo = "https://github.com/Kayoshi-dev/SimpleOOPDashboard"

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

#This function clone a repository
def gitClone():
    try:
        subprocess.check_call(['git', 'clone', urlRepo])
        print('Downloading the Github repository...')
        print('Finished!💪')
    except subprocess.CalledProcessError as e:
        print('An error has occurred : ', e.returncode)

gitClone()