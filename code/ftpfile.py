# Fetch and open/play a file by FTP

import webbrowser, sys
from ftplib import FTP                       # socket-based FTP tools
from getpass import getpass                  # hidden password input
if sys.version[0] == '2': input = raw_input  # 2.X compatibility

nonpassive = False                           # force active mode FTP for server?
filename   = input('File?')                  # file to be downloaded
dirname    = input('Dir? ') or '.'           # remote directory to fetch from
sitename   = input('Site?')                  # FTP site to contact
user       = input('User?')                  # use () for anonymous
if not user:
    userinofo = ()
else:
    from getpass import getpass              # hidden password input
    userinfo = (user, getpass('Pswd?'))   

print('Connecting...')
connection = FTP(sitename)                   # connect to FTP site
connection.login(*userinfo)                  # default is anonymous login
connection.cwd(dirname)                      # xfer 1k at a time to localfile
if nonpassive:                               # force active FTP if server requires
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')             # local file to store download
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

print('Playing...')
webbrowser.open(filename)
