#Kyle Pendleton
#04/11/2024
#This will check for login pages of the website

import requests

site_logins = []

# open file and read the content in a list
with open('Logins.txt', 'r') as filehandle:
    for line in filehandle:
        login_pages = line[:-1]
        site_logins.append(login_pages)

website = "https://www.amazon.com"

for login in site_logins:
	print("Checking... "+ website + login)
	reply = requests.get(website + login)
	if reply.status_code == 200:
		print("Login resource detected: " +login)