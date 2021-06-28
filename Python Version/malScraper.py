from colorama import Fore, Back, Style
import pyfiglet

#formatting
RED='\033[0;31m' #red
GRN='\033[0;32m' #green
NC='\033[39m' #no colour 
BOLD='\033[1m' #bold
Purple='\033[1;35m' #purple
Cyan='\033[1;36m' #cyan
Yellow='\033[1;33m' #yellow
banner = pyfiglet.figlet_format("malScraper", font = "slant")

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