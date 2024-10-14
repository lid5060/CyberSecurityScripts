#Kyle Pendleton
#14/10/2024
#This request will get the html response from a specified website
#!/usr/bin/env python3

import requests, json
website = input("Enter the hostname http://")
result = requests.get("http://"+website)
print(result.json)
print("Status code: "+str(result.status_code))
print("Headers response: ")
for header, value in result.headers.items():
  print(header, '-->', value)
print("Headers request : ")
for header, value in result.request.headers.items():
  print(header, '-->', value)