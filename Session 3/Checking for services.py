# Checking for services.py
# Kyle Pendleton
# 07/10/2024
# This will check if the specified ports are open or closed and then output the result with a open or closed message

#!/usr/bin/python
import socket
ip_address = '127.0.0.1'
list_of_ports = [79, 70, 194, 138, 25]
for port in list_of_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for port in list_of_ports:
    output = sock.connect_ex((ip_address, port))
    if output == 0:
        print("Port", port, ": Open")
    else:
        print("Port", port, ": Closed")
    sock.close()