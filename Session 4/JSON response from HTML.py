#Kyle Pendleton
#14/10/2024
#This request will get json response from a specified website
#!/usr/bin/env python3

import urllib.request
import json

Website_Link = "http://httpbin.org/get"

with urllib.request.urlopen(Website_Link) as Reply:
    Website_Data = json.loads(Reply.read().decode("utf-8"))
    print(Website_Data)