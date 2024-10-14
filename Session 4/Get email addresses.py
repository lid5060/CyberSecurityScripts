#Kyle Pendleton
#14/10/2024
#This request will get email addresses from the website
import urllib.request
import re

UserAgent = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'

Website = input("Enter url:")

#https://mail.python.org/mailman3/lists/python-dev.python.org

website_opener = urllib.request.build_opener()
website_opener.addheaders = [('User-agent', UserAgent)]
urllib.request.install_opener(website_opener)
output = urllib.request.urlopen(Website)
html_result = output.read()
patterns = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
email_addresses = re.findall(patterns,str(html_result))
print(email_addresses)