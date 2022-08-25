import sys
import iptocc
import logging

index = 0
ips = open("extracted/uniqueIPs.txt", "r").readlines()
countries = {}
logger = logging.getLogger("iptocc")
logger.propagate = False

print("Setting up IP range database...")
iptocc.get_country_code("8.8.8.8")
print("Querying IP addresses...")

for ip in ips:

  # update progress every 5 IPs
  if index % 5 == 0:
    sys.stdout.write("\rProgress - %s%%" % str(round(100 * index/len(ips), 2)))
    sys.stdout.flush()

  originCountry = iptocc.get_country_code(ip[:-1])
  if originCountry not in countries:
    countries[originCountry] = 1
    continue

  countries[originCountry] += 1
  index += 1
