#Kyle Pendleton
#11/11/2024
#This script will list all the files in the specified ftp directory

#!/usr/bin/env python3

from ftplib import FTP

ftp_server=FTP('ftp.be.debian.org')
print("Server: ",ftp_server.getwelcome())
print(ftp_server.login())
print("Files and directories in the root directory:")
ftp_server.dir()

ftp_server.cwd('/www.kernel.org/pub/linux/kernel/v6.x/')
ftp_files=ftp_server.nlst()
ftp_files.sort()
print("%d files in /pub/linux/kernel directory:"%len(ftp_files))
for file in ftp_files:
	print(file)

ftp_server.quit()