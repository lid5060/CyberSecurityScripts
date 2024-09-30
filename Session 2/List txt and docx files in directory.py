#!/usr/bin/env python3
import os
try:
    for file in os.listdir('.'):
        if file.endswith('.txt') or file.endswith('.docx'):
            print(file)
except:
    print("An error occurred")
# List txt and docx files in directory.py
# Kyle Pendleton
# 30/09/2024
# This will list all the txt and docx files in the directory where the programme is running from