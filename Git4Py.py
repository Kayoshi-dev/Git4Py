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

    print('-------------------------------------')

    #If you want to setup a database:
    #Maybe I should turn this into a function.
    if os.path.exists(os.getcwd() + os.sep + 'config.ini'):
        print('Todo!')
        #TODO
    else:
        try:
            print('Creating a new config file... ⌛')
            config = open('config.ini', 'w+')
            print('Done! ✔')
            print('-------------------------------------')
            response = None
            while response != 'Y' or response != 'N':
                response = input('Would you like to link your database now ? (Y/N)').upper()
                if response == 'Y':
                    host = input('Host :')
                    user = input('User :')
                    password = input('Password :')
                    config.write('[database] \n'
                                 'host=' + host + '\n'
                                 'user=' + user + '\n'
                                 'password=' + password + '\n')
                    config.close()
                    break
                if response == 'N':
                    config.write('[database] \n'
                                 'host=\n'
                                 'user=\n'
                                 'password=\n')
                    config.close()
                    break
            print('Done! ✔')
            print('-------------------------------------')
        except (OSError, IOError) as e:
            print(e.returncode)
    gitClone()

#This function clone a repository
def gitClone():
    #If the directory exist, or if we already are in the directory named like the repository
    if os.path.exists(os.getcwd() + os.sep + dirname) or os.getcwd().split(os.sep)[-1] == dirname:
        os.chdir(dirname)
        try:
            pullResult = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
            print('The repository directory already exist...')
            print('Updating... ⌛')
            while True:
                line = pullResult.stdout.readline()
                if not line:
                    break
                print(line)
            print('Done! ✔')
            print('-------------------------------------')
        except subprocess.CalledProcessError as e:
            print('❌ An error has occurred : ', e.returncode)
    else:
        try:
            cloneResult = subprocess.Popen(['git', 'clone', urlRepo], stdout=subprocess.PIPE)
            print('Downloading the Github repository... ⌛')
            while True:
                line = cloneResult.stdout.readline()
                if not line:
                    break
                print(line)
            print('Finished! 💪')
            print('-------------------------------------')
        except subprocess.CalledProcessError as e:
            print('❌ An error has occurred : ', e.returncode)

gitMain()