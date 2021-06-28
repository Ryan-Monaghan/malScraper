import os
import pyfiglet
import getpass
from time import sleep
from datetime import datetime
import subprocess as sp
import importlib.util
import sys
import zipfile
import random

#formatting
RED='\033[0;31m' #red
GRN='\033[0;32m' #green
NC='\033[39m' #no colour 
BOLD='\033[1m' #bold
Purple='\033[1;35m' #purple
Cyan='\033[1;36m' #cyan
Yellow='\033[1;33m' #yellow
currentVersion=1.0
banner = pyfiglet.figlet_format("malScraper", font = "slant")

#Get current user
def getUser():
    username = getpass.getuser()
    return username

#splash-text arrays
#todo

#time-on-run
currTime=datetime.now()
timeStamp=currTime.strftime('%Y-%m-%d-%H:%M')
#print(timeStamp)

#data locations
#stores the default location of the download path of the various feeds - these can be modified to custom locations
PayloadReport = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\PayloadReport.txt")
C2Report = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\C2Report.txt")
Top100 = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\Top100Report.txt")
HexReport = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\HexReport.txt")
HausMalDown = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\HausMalDown")
PhishTank = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\PhishTank.csv")
tempFile = ("C:\\Users\\" + getUser() + "\\Desktop\\malScraper\\temp.zip")

#feed locations
PayloadFeed=https://urlhaus.abuse.ch/downloads/text/
C2Feed=cybercrime-tracker.net/all.php
HexFeed=http://tracker.h3x.eu/api/sites_1month.php
PhishTank=http://data.phishtank.com/data/online-valid.csv
#HausMalDown=https://urlhaus.abuse.ch/downloads/csv/

#GitHub CodeLoad API
release=https://api.github.com/repos/Ryan-Monaghan/malScraper/releases/latest

print(banner)

print(BOLD + Purple + '\tTOOL\t' + '::' + 'malScraper')
print('\tAuthor\t' + '::' + 'Ryan Monaghan')
print('\tTwitter\t' + '::' + '@RyanSecOps')
print('\tGithub\t' + '::' + 'https://github.com/Ryan-Monaghan/malScraper')
print('\tBranch\t' + '::' + 'Experimental')
print('\tVersion\t' + '::' + '1.0\n' + NC)

print(Cyan + 'HELP MENU' + NC + ' :: ' + 'Available ' + Yellow + 'options ' + NC + 'shown below:\n ')

print(' [*] ' + Cyan + 'Tutorial ' + NC + 'of how to use this tool\t\t\t\t\t' + Yellow + 'TUTORIAL' + NC)
print(' [*] ' + 'Show this '+ Cyan + 'Help ' + NC + 'Menu\t\t\t\t\t\t' + Yellow + 'HELP,GET-HELP,?,-?,/?' + NC)
print(' [*] ' + Cyan + 'Show options ' + NC + 'for this tool\t\t\t\t\t\t' + Yellow + 'SHOW OPTIONS,SHOW,OPTIONS' + NC)
print(' [*] ' + Cyan + 'Clear ' + NC + 'screen\t\t\t\t\t\t\t' + Yellow + 'CLEAR,CLEAR-HOST,CLS' + NC)
print(' [*] ' + 'Return to ' + Cyan + 'Home ' + NC + 'Menu\t\t\t\t\t\t' + Yellow + 'HOME,BACK,CD ..' + NC)
print(' [*] ' + Cyan + 'Open ' + Cyan + NC + 'an existing report\t\t\t\t\t\t' + Yellow + 'OPEN,REOPEN' + NC)
print(' [*] ' + Cyan + 'Quit ' + NC + 'malScraper\t\t\t\t\t\t\t' + Yellow + 'QUIT,EXIT' + NC)
print(' [*] ' + Cyan + 'Install ' + NC + 'the latest ' + Cyan + 'update\t\t\t\t\t\t' + NC + Yellow + 'INSTALL,UPDATE' + NC)
print(' [*] ' + 'Perform ' + Cyan + 'Full-Scan ' + NC + '(Note this may take some time)\t\t\t' + Yellow + 'FULL,FULL-SCAN,FSCAN' + NC)
print(' [*] ' + 'Perform ' + Cyan + 'Quick-Scan ' + NC + '(Most recent 100 Payload Domains)\t\t' + Yellow + 'QUICK,QUICK-SCAN,QSCAN' + NC)