#Kyle Pendleton
#11/11/2024
#This script will download the specified file from the ftp server

#!/usr/bin/env python3

import ftplib

FTP_SERVER_ADDRESS = 'ftp.be.debian.org'
DOWNLOAD_FILE = 'www.kernel.org/pub/linux/kernel/v6.x/'
DOWNLOAD_NAME = 'ChangeLog-6.9.9'

def ftp_file_downloader(ftp_server, ftp_username):
    ftp_client_settings = ftplib.FTP(ftp_server, ftp_username)
    ftp_client_settings.cwd(DOWNLOAD_FILE)
    try:
        with open(DOWNLOAD_NAME, 'wb') as file_handler:
            ftp_command = 'RETR %s' %DOWNLOAD_FILE
            ftp_client_settings.retrbinary(ftp_command,file_handler.write)
            ftp_client_settings.quit()
    except Exception as exception:
        print('File could not be downloaded:',exception)

if __name__ == '__main__':
    ftp_file_downloader(ftp_server=FTP_SERVER_ADDRESS,ftp_username='anonymous')