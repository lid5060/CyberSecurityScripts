#Kyle Pendleton
#14/10/2024
#This request will download the specified image from the website
#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil
import requests

website = 'https://www.uclan.ac.uk/image-library/content/research/Student-centre-rooftop-students-2.x2157f597.jpeg'
reply = requests.get(website, stream=True)
with open('Student-centre-rooftop-students-2.x2157f597.jpeg', 'wb') as picture:
    shutil.copyfileobj(reply.raw, picture)