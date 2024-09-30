#!/usr/bin/env python3
from future.backports import count

try:
    numoflines = numofchars = 0
    file = open('grumpy.txt', 'r')
    lines = file.readlines()
    for line in lines:
        numoflines += 1
        for char in line:
            numofchars += 1
    file.close()
    print("Characters in file:", numofchars)
    print("Lines in file:", numoflines)
except FileNotFoundError as error:
    print("File could not be found:", str(error))
# Count all lines in text file.py
# Kyle Pendleton
# 30/09/2024
# This will count all the lines in a text file