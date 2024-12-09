#Kyle Pendleton
#09/12/2024
#This script will find the password for a zip file using a specified dictionary file

import zipfile

name_of_file = 'output.zip'
dictionary_file = 'password_list.txt'

my_file = zipfile.ZipFile(name_of_file)
with open(dictionary_file, 'r') as f:
	for line in f.readlines():
		password_result = line.strip('\n')
		try:
			my_file.extractall(pwd=bytes(password_result,'utf-8'))
			print('Password found: %s' % password_result)
		except Exception as exception:
			print("Trying password:%s Exception:%s" % (password_result,exception))