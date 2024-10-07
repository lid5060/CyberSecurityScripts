# Returning network information.py
# Kyle Pendleton
# 07/10/2024
# This will return information about the specified network address

#!/usr/bin/python
import socket
hostname = socket.gethostname()
print("Hostname:", hostname)
IP = socket.gethostbyname(hostname)
print("Your IP address:", IP)
print("Host IP address", socket.gethostbyname('www.mancity.com'))
print("Alternative addresses:", socket.gethostbyname_ex('www.mancity.com'))
print("DNS server used:", socket.gethostbyaddr('8.8.8.8'))
print("Fully qualified domain name:", socket.getfqdn('www.google.com'))
print("Address information:", socket.getaddrinfo("www.google.com", None, 0, socket.SOCK_STREAM))