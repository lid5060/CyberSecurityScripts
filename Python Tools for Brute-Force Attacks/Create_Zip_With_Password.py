#Kyle Pendleton
#09/12/2024
#This script will create a zip folder that is password protected

import pyminizip

user_input = "files/file.txt"
user_output = "output.zip"
user_password = "my_password"
selected_compresion_level = 5

pyminizip.compress(user_input, None, user_output, user_password, selected_compresion_level)