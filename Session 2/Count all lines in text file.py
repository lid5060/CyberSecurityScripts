#!/usr/bin/env python3
from future.backports import count

try:
    numoflines = numofchars = 0
    file = open('grumpy.txt', 'r')
# this will open the separate file in read mode so that the file can be read
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
# 30/09/2024