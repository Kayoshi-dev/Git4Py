#!/usr/bin/python3
# -*- coding: utf-8 -*-

#   Simple Python 3 script to interact with a Github repository

import subprocess, os, glob, io

#   TODO read these information from the config.ini file
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

    FirstUse()


#   This function is automatically called when the script is used for the first time
def FirstUse():
    responseRepo = None
    while responseRepo != 'Y' or responseRepo != 'N':
        responseRepo = input('Would you like to attach this script to your Github repository ? (Y/N)').upper()
        if responseRepo == 'Y':
            urlRepo = input('Please paste the link to your Github repository :')
            print('Creating a new config file... ⌛')
            config = open('config.ini', 'w+')
            config.write('[Repository] \n'
                         'urlRepo = ' + urlRepo + '\n \n')
            config.close()
            print('Done! ✔')
            print('-------------------------------------')
            break
        if responseRepo == 'N':
            print('Note that most of the functionalities will not work without your URL repository')
            config = open('config.ini', 'w+')
            config.write('[repository] \n'
                         'urlRepo = \n \n')
            print('-------------------------------------')
            break
    setupDatabase()


#   This function help you to correctly setup a database
def setupDatabase():
    if os.path.exists(os.getcwd() + os.sep + 'config.ini'):
        with open('config.ini', 'r+') as f:
            for line in f:
                if '[database]' in line:
                    print('Your Database in already linked.')
                    break
            else:
                try:
                    print('Opening the configuration file...')
                    config = open('config.ini', 'a+')
                    print('-------------------------------------')
                    response = None
                    while response != 'Y' or response != 'N':
                        response = input('Would you like to link your database now ? (Y/N)').upper()
                        if response == 'Y':
                            host = input('Host :')
                            user = input('User :')
                            password = input('Password :')
                            config.write('[database] \n'
                                         'host =' + host + '\n'
                                         'user =' + user + '\n'
                                         'password =' + password + '\n')
                            config.close()
                            break
                        if response == 'N':
                            config.write('[database] \n'
                                         'host =\n'
                                         'user =\n'
                                         'password =\n')
                            config.close()
                            break
                    print('Done! ✔')
                    print('-------------------------------------')
                except (OSError, IOError) as e:
                    print(e.returncode)
    else:
        try:
            open('config.ini', 'w+')
        except (OSError, IOError) as e:
            print(e.returncode)
        setupDatabase()

#   This function clone a repository
def gitClone():
    #   If the directory exist, or if we already are in the directory named like the repository
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
