#!/usr/bin/env python3
import zipfile
try:
    def List_all_files_in_zip(filename):
        with zipfile.ZipFile(filename) as myzip:
            for zipinfo in myzip.infolist():
                yield zipinfo.filename
# the function List_all_files_in_zip will list all the files in the zip file
    for filename in List_all_files_in_zip("files.zip"):
        print(filename)
# when the code is ran the output will be printed to the screen to show which files are in the zip file
except:
    print("An error occurred")
# try and except will handle an error if one occurs and print out an error message
# 30/09/2024