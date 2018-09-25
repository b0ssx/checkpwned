#***********************************************************************************
#*       Written by: B0ssx                                                         *
#*       Github    : https://github.com/b0ssx                                      *
#*       Python script to check for pwned email addresses                          *
#***********************************************************************************

import sys
import os,argparse,requests
from colorama import init
init()                        #Needed for Windows ansi colours to display correctly
UserAgent = {'User-Agent': 'B0ssx Fr@m3w0rk'}

#Function to check email address against www.haveibeenpwned.com
def qcheck_haveibeenpwned(email):
    url = "https://haveibeenpwned.com/api/v2/breachedaccount/" + str(email)
    req = requests.get(url, headers=UserAgent)

    try:
        if  req.status_code==200:
            print("\033[31m" + "**PWNED** " + "\033[33m"  + email + "\033[30m")
            results = open("results.txt","a")
            results.write("\n" + email)
            results.close()
        else:
            print( email + " have not been pwned")
    except:
       print(" Oops..")

#Cmdline arg parser. only chekc for email file name and store as var filename
parser = argparse.ArgumentParser(prog='checkpwned.py')
parser.add_argument("filename", help="Text filename with email addresses to check")
args = parser.parse_args()
filename = args.filename

#Read emails from file
with open(filename, 'r') as infile:
    data = infile.read()
email_list = data.splitlines()

try:
    #Create new results.txt file in current location
    results = open("results.txt","w")
    results.write( "Pwned Email results .... >" + "\n")
    results.close()
except:
    print("Cannot create results.txt file!")

#Set console colours
print("")
print("\033[37m" + "Testing emails.....>" + "\033[30m")

#Read emails from file and pass to func
for email in email_list:
    qcheck_haveibeenpwned(email)
print("")
print("\033[37m" + "Pwned emails address saved to results.txt")

