import iptocc

ips = open("extracted/uniqueIPs.txt", "r").readlines()
countries = {}

for ip in ips:
  originCountry = iptocc.get_country_code(ip[:-1])
  print("origin:", originCountry)
  if originCountry not in countries:
    countries[originCountry] = 1
    continue
  
  countries[originCountry] += 1
