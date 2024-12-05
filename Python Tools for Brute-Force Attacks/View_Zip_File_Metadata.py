#Kyle Pendleton
#09/12/2024
#This script will list the metadata information of a specified zip folder

import datetime
import zipfile
zf = zipfile.ZipFile("zipfile.zip", "r")
for information in zf.infolist():
    print(information.filename)
    print("  Comment: " + str(information.comment.decode()))
    print("  Modified: " + str(datetime.datetime(*information.date_time)))
    print("  System: " + str(information.create_system) + " (0=MS-DOS OS-2, 3=Unix)")
    print("  ZIP version: " + str(information.create_version))
    print("  Compressed: " + str(information.compress_size) + " bytes")
    print("  Uncompressed: " + str(information.file_size) + " bytes")
zf.close()