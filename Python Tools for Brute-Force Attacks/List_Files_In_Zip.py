#Kyle Pendleton
#09/12/2024
#This script will list all files in a specified zip folder

import zipfile

zf = zipfile.ZipFile("zipfile.zip", "r")
print(zf.namelist())
zf.close()