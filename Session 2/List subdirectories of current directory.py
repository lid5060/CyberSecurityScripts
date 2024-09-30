#!/usr/bin/env python3
import os
try:
    for root, directories, files in os.walk(".", topdown=False):
        for file_entry in files:
            print('[+] ', os.path.join(root, file_entry))
        for name in directories:
            print('[++] ', name)
except:
    print("An error occurred")
# List subdirectories of current directory.py
# Kyle Pendleton
# 30/09/2024
# This will list all the subdirectories of the current directory where the programme is running from