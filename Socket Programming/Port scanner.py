# Port scanner.py
# Kyle Pendleton
# 07/10/2024
# This will scan a specified network for open ports

#!/usr/bin/env python
import socket
import errno
Remote_connection = input("Enter a remote network to scan: ")
Remote_connection_IP = socket.gethostbyname(Remote_connection)
print("Please enter the range of ports you would like to scan on the machine")
Staring_port = input("Enter port to start with: ")
Ending_port = input("Enter port to end with: ")
print("Please wait, scanning remote host", Remote_connection_IP)
for port in range(int(Staring_port),int(Ending_port)):
    print ("Checking port {} ...".format(port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((Remote_connection_IP, port))
    if result == 0:
        print("Port: Open".format(port))
    else:
        print("Port: Closed".format(port))
        print("Reason:",errno.errorcode[result])
        sock.close()