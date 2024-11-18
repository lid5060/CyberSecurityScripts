# Returning network information and port scanning.py
# Kyle Pendleton
# 07/10/2024
# This is a combination of the network information and port scanning scripts

#!/usr/bin/env python
import socket
import errno
#returning network information section
Host = input("Enter a remote network to scan: ")
hostname = socket.gethostname()
print("Hostname:", hostname)
IP = socket.gethostbyname(hostname)
print("Your IP address:", IP)
print("Host IP address", socket.gethostbyname(Host))
print("Alternative addresses:", socket.gethostbyname_ex(Host))
print("DNS server used:", socket.gethostbyaddr('8.8.8.8'))
print("Fully qualified domain name:", socket.getfqdn('www.google.com'))
print("Address information:", socket.getaddrinfo("www.google.com", None, 0, socket.SOCK_STREAM))
#port scanning section
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