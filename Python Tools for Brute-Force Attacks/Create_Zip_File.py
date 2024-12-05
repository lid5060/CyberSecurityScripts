#Kyle Pendleton
#09/12/2024
#This script will create a zip file

import os
import zipfile

zf = zipfile.ZipFile("newzipfile.zip", "w")
for dirname, subdirs, files in os.walk('files', topdown=False):
    for file_name in files:
        print(file_name)
        zf.write(os.path.join(dirname, file_name))
zf.close()