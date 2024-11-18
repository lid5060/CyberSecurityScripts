#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user=input("Enter username:")
user_password = getpass()

reply = requests.get('https://www.mancity.com/', auth=HTTPBasicAuth(user,user_password))
print('Response.status_code:'+ str(reply.status_code))

if reply.status_code == 200:
    print('Login successful :'+reply.text)
elif reply.status_code == 403:
    print('Login unsuccessful :'+reply.text)