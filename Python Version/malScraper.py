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
print('\tTwitter\t' + '::' + '@rynmonaghan')
print('\tGithub\t' + '::' + 'https://github.com/Ryan-Monaghan/malScraper')
print('\tBranch\t' + '::' + 'Experimental')
print('\tVersion\t' + '::' + '1.0\n' + NC)

print(Cyan + 'HELP MENU' + NC + ' :: ' + 'Available ' + Yellow + 'options ' + NC + 'shown below:\n ')

print(' [*] ' + Cyan + 'Tutorial ' + NC + 'of how to use this tool')
print(' [*] ' + 'Show this '+ Cyan + 'Help ' + NC + 'Menu')
print(' [*] ' + Cyan + 'Show options ' + NC + 'for this tool')
print(' [*] ' + Cyan + 'Clear ' + NC + 'screen')
print(' [*] ' + Cyan + 'Open ' + Cyan + NC + 'an existing report')
print(' [*] ' + Cyan + 'Quit ' + NC + 'malScraper')
print(' [*] ' + Cyan + 'Install ' + NC + 'the latest ' + Cyan + 'update' + NC)
print(' [*] ' + 'Perform ' + Cyan + 'Full-Scan ' + NC + '(Note this may take some time) ')
print(' [*] ' + 'Perform ' + Cyan + 'Quick-Scan ' + NC + '(Most recent 100 Payload Domains)')