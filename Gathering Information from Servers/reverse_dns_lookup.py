#Kyle Pendleton
#04/11/2024
#This will perform a reverse DNS request on the specified IP

import dns.reversename

IP_Address = dns.reversename.from_address("13.35.99.137")
print(IP_Address)
print(dns.reversename.to_address(IP_Address))