#!/usr/bin/env python3
import zipfile
try:
    def List_all_files_in_zip(filename):
        with zipfile.ZipFile(filename) as myzip:
            for zipinfo in myzip.infolist():
                yield zipinfo.filename
    for filename in List_all_files_in_zip("files.zip"):
        print(filename)
except:
    print("An error occurred")

# List all files in zip folder.py
# Kyle Pendleton
# 30/09/2024
# This will list all the files in a zip folder