import getpass
from datetime import datetime
import subprocess as sp
import importlib.util
import sys
import zipfile
import random
import pyfiglet
from os import system, name
from time import sleep


########################################################
# function responsible for clearing users screen on call#
########################################################
def clear():
    system('cls')
    # helptext()
    useroptions()


# formatting
RED = '\033[0;31m'  # red
GREEN = '\033[0;32m'  # green
NC = '\033[39m'  # no colour
BOLD = '\033[1m'  # bold
PURPLE = '\033[1;35m'  # purple
CYAN = '\033[1;36m'  # cyan
YELLOW = '\033[1;33m'  # yellow
currentVersion = 1.0
banner = pyfiglet.figlet_format("malScraper", font="slant")


# Get current user
def getuser():
    username = getpass.getuser()
    return username


# splash-text arrays
# todo

# time-on-run
currTime = datetime.now()
timeStamp = currTime.strftime('%Y-%m-%d-%H:%M')
# print(timeStamp)

# data locations
# stores the default location of the download path of the various feeds - these can be modified to custom locations
PayloadReport = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\PayloadReport.txt")
C2Report = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\C2Report.txt")
Top100 = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\Top100Report.txt")
HexReport = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\HexReport.txt")
HausMalDown = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\HausMalDown.csv")
PhishTank = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\PhishTank.csv")
tempFile = ("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\temp.zip")


# feed locations
# PayloadFeed=https://urlhaus.abuse.ch/downloads/text/
# C2Feed=cybercrime-tracker.net/all.php
# HexFeed=http://tracker.h3x.eu/api/sites_1month.php
# PhishTank=http://data.phishtank.com/data/online-valid.csv
# HausMalDown=https://urlhaus.abuse.ch/downloads/csv/

# GitHub CodeLoad API
# release=https://api.github.com/repos/Ryan-Monaghan/malScraper/releases/latest

# print(banner)
#
# print(BOLD + PURPLE + '\tTOOL\t' + ':: ' + 'malScraper')
# print('\tAuthor\t' + ':: ' + 'Ryan Monaghan')
# print('\tTwitter\t' + ':: ' + '@RyanSecOps')
# print('\tGithub\t' + ':: ' + 'https://github.com/Ryan-Monaghan/malScraper')
# print('\tBranch\t' + ':: ' + 'Experimental')
# print('\tVersion\t' + ':: ' + '1.0\n' + NC)
#
# print(CYAN + 'HELP MENU' + NC + ' :: ' + 'Available ' + YELLOW + 'options ' + NC + 'shown below:\n ')
#
# print(' [*] ' + CYAN + 'Tutorial ' + NC + 'of how to use this tool\t\t\t\t\t' + YELLOW + 'TUTORIAL' + NC)
# print(' [*] ' + 'Show this ' + CYAN + 'Help ' + NC + 'Menu\t\t\t\t\t\t' + YELLOW + 'HELP,GET-HELP,?,-?,/?' + NC)
# print(' [*] ' + CYAN + 'Show options ' + NC + 'for this tool\t\t\t\t\t\t' + YELLOW + 'SHOW OPTIONS,SHOW,OPTIONS' + NC)
# print(' [*] ' + CYAN + 'Clear ' + NC + 'screen\t\t\t\t\t\t\t' + YELLOW + 'CLEAR,CLEAR-HOST,CLS' + NC)
# print(' [*] ' + 'Return to ' + CYAN + 'Home ' + NC + 'Menu\t\t\t\t\t\t' + YELLOW + 'HOME,BACK,CD ..' + NC)
# print(' [*] ' + CYAN + 'Open ' + CYAN + NC + 'an existing report\t\t\t\t\t\t' + YELLOW + 'OPEN,REOPEN' + NC)
# print(' [*] ' + CYAN + 'Quit ' + NC + 'malScraper\t\t\t\t\t\t\t' + YELLOW + 'QUIT,EXIT' + NC)
# print(
#    ' [*] ' + CYAN + 'Install ' + NC + 'the latest ' + CYAN + 'update\t\t\t\t\t\t' + NC + YELLOW + 'INSTALL,UPDATE' + NC)
# print(
#    ' [*] ' + 'Perform ' + CYAN + 'Full-Scan ' + NC + '(Note this may take some time)\t\t\t' + YELLOW + 'FULL,FULL-SCAN,FSCAN' + NC)
# print(
#    ' [*] ' + 'Perform ' + CYAN + 'Quick-Scan ' + NC + '(Most recent 100 Payload Domains)\t\t' + YELLOW + 'QUICK,QUICK-SCAN,QSCAN' + NC)


# this function stored the download path of each feed, and prints to screen when called
def dirlist():
    print(GREEN + '\nSuccess - Files written to:\n' + NC)
    print(GREEN + '1. ' + RED + 'Payload Domains:' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\PayloadReport.txt\n")
    print(GREEN + '2. ' + RED + 'AMP Report:' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\PayloadReport.txt\n")
    print(GREEN + '3. ' + RED + 'C2 Servers:' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\C2Report.txt\n")
    print(GREEN + '4. ' + RED + 'Hex Report:' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\HexReport.txt\n")
    print(GREEN + '5. ' + RED + 'URLHaus Maldownloads' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\HausMalDown.csv\n")
    print(GREEN + '6. ' + RED + 'PhishTank Phishing Pages:' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\PhishTank.csv\n")
    print(GREEN + '7. ' + RED + 'Most Recent 100:' + NC)
    print("C:\\Users\\" + getuser() + "\\Desktop\\malScraper\\Top100Report.txt\n")


###############################################################################
# function responsible for storing the help text for usage in the help function#
###############################################################################
def helptext():
    print(CYAN + 'HELP MENU' + NC + ' :: ' + 'Available ' + YELLOW + 'options ' + NC + 'shown below:\n ')

    print(' [*] ' + CYAN + 'Tutorial ' + NC + 'of how to use this tool\t\t\t\t\t' + YELLOW + 'TUTORIAL' + NC)
    print(' [*] ' + 'Show this ' + CYAN + 'Help ' + NC + 'Menu\t\t\t\t\t\t' + YELLOW + 'HELP,GET-HELP,?,-?,/?' + NC)
    print(
        ' [*] ' + CYAN + 'Show options ' + NC + 'for this tool\t\t\t\t\t\t' + YELLOW + 'SHOW OPTIONS,SHOW,OPTIONS' + NC)
    print(' [*] ' + CYAN + 'Clear ' + NC + 'screen\t\t\t\t\t\t\t' + YELLOW + 'CLEAR,CLEAR-HOST,CLS' + NC)
    print(' [*] ' + 'Return to ' + CYAN + 'Home ' + NC + 'Menu\t\t\t\t\t\t' + YELLOW + 'HOME,BACK,CD ..' + NC)
    print(' [*] ' + CYAN + 'Open ' + CYAN + NC + 'an existing report\t\t\t\t\t\t' + YELLOW + 'OPEN,REOPEN' + NC)
    print(' [*] ' + CYAN + 'Quit ' + NC + 'malScraper\t\t\t\t\t\t\t' + YELLOW + 'QUIT,EXIT' + NC)
    print(
        ' [*] ' + CYAN + 'Install ' + NC + 'the latest ' + CYAN + 'update\t\t\t\t\t\t' + NC + YELLOW + 'INSTALL,UPDATE' + NC)
    print(
        ' [*] ' + 'Perform ' + CYAN + 'Full-Scan ' + NC + '(Note this may take some time)\t\t\t' + YELLOW + 'FULL,FULL-SCAN,FSCAN' + NC)
    print(
        ' [*] ' + 'Perform ' + CYAN + 'Quick-Scan ' + NC + '(Most recent 100 Payload Domains)\t\t' + YELLOW + 'QUICK,QUICK-SCAN,QSCAN' + NC)


###########################################################
# function responsible for printing the help menu to screen#
###########################################################
def help():
    helptext()
    useroptions()


#####################################################################
# function responsible for printing the usage tutorial menu to screen#
#####################################################################
# def tutorial():
# print('Unfinished.')
# useroptions()

########################################################################
# this function allows the user to reopen a previously downloaded report#
########################################################################
# def reopen():

###############################################
# function responsible for checking for updates#
# queries GitHub CodeLoad API to verify version#
###############################################
# def versioncheck():

# this function is responsible for handling program exits
def exit():
    close = input("Are you sure? (Y/N)")
    close = close.upper()
    if close == "Y" or close == "YES":
        system('cls')
        quit()
    elif close == "N" or close == "NO":
        print("\n")
        useroptions()
    else:
        clear()
        print(RED + "Error - " + NC + "invalid operation\n\n")
        system('cls')
        helptext()
        useroptions()


def useroptions():
    read = input("\nmalscraper>")
    read = read.upper()
    if read == "FULL" or read == "FULL-SCAN" or read == "FSCAN":
        #fullscan()
        print("This menu is TODO")
        sleep(2)
        main()
    elif read == "QUICK" or read == "QUICK-SCAN" or read == "QSCAN":
        #quickscan()
        print("This menu is TODO")
        sleep(2)
        main()
    elif read == "QUIT" or read == "EXIT":
        exit()
    elif read == "CLEAR" or read == "CLEAR-HOST" or read == "CLS":
        clear()
    elif read == "HELP" or read == "GET-HELP" or read == "?" or read == "-?" or read == "/?" or read == "MENU":
        helptext()
    elif read == "BACK" or read == "CD .." or read == "HOME":
        main()
    elif read == "TUTORIAL":
        #tutorial()
        print("This menu is TODO")
        sleep(2)
        main()
    elif read == "REOPEN" or read == "OPEN":
        #reopen()
        print("This menu is TODO")
        sleep(2)
        main()
    elif read == "INSTALL" or read == "UPDATE":
        #installupdate()
        print("This menu is TODO")
        sleep(2)
        main()
    else:
        system('cls')
        print(RED + "Error - " + NC + "invalid operation\n\n")
        helptext()
        useroptions()


###########################################################
# function responsible for printing the main menu to screen#
###########################################################
def main():
    system('cls')
    # versioncheck()
    # clear()
    print(banner)
    print(BOLD + PURPLE + '\tTOOL\t' + ':: ' + 'malScraper')
    print('\tAuthor\t' + ':: ' + 'Ryan Monaghan')
    print('\tTwitter\t' + ':: ' + '@RyanSecOps')
    print('\tGithub\t' + ':: ' + 'https://github.com/Ryan-Monaghan/malScraper')
    print('\tBranch\t' + ':: ' + 'Experimental')
    print('\tVersion\t' + ':: ' + '1.0\n' + NC)
    helptext()
    useroptions()


main()
