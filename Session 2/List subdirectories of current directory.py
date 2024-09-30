#!/usr/bin/env python3
try:
    import os
    for root, directories, files in os.walk(".", topdown=False):
        for files_found in files:
            print('[+] ',os.path.join(root, files_found))
# the files in the current directory will be printed to the screen
        for name in directories:
            print('[++] ',name)
# the directories in the current directory will be printed to the screen
# os.walk will list all the files in the current directory and then printed to the screen
except:
    print("An error occurred")