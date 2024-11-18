#Kyle Pendleton
#04/11/2024
#This will receive the DNS data about the specified website

import dns.resolver

def main(domain_name):
    domain_records = ['A','AAAA','NS','SOA','MX','TXT','CNAME','PTR']
    for record in domain_records:
        try:
            responses = dns.resolver.resolve(domain_name, record)
            print("\nRecord response ",record)
            print("-----------------------------------")
            for response in responses:
                print(response)
        except Exception as exception:
            print("Cannot resolve query for record",record)
            print("Error for obtaining record information:", exception)

if __name__ == '__main__':
	try:
		main('www.amazon.com')
	except KeyboardInterrupt:
		exit()