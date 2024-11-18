#Kyle Pendleton
#11/11/2024
#This script will check to see if the ftp server can be accessed through anonymous login

#!/usr/bin/env python3

import ftplib

def anonymousLogin(domain):
    try:
        ftp_server = ftplib.FTP(domain)
        reply = ftp_server.login('anonymous', 'anonymous')
        print(reply)
        if "230 Anonymous access granted" in reply:
            print('\n[*] ' + str(domain) +' FTP Anonymous Login Succeeded.')
            print(ftp_server.getwelcome())
            ftp_server.dir()
    except Exception as exception:
        print(str(exception))
        print('\n[-] ' + str(domain) +' FTP Anonymous Login Failed.')

domain = 'ftp.be.debian.org'
anonymousLogin(domain)