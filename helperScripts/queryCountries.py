import sys
import iptocc
import logging
import json
from math import isnan

index = 0
ips = open("extracted/uniqueIPs.txt", "r").readlines()
countries = {"NaN": 0}
logger = logging.getLogger("iptocc")
logger.propagate = False

# Initialize IP db
print("Setting up IP range database...")
iptocc.get_country_code("8.8.8.8")
print("Querying IP addresses...")


for ip in ips:

  # update progress every 5 IPs
  if index % 5 == 0:
    sys.stdout.write("\rProgress - %s%%" % str(round(100 * index/len(ips), 2)))
    sys.stdout.flush()

  # Handle invalid IP address
  try: originCountry = iptocc.get_country_code(ip[:-1])
  except: print("Error parsing " + ip + ". Skipping.")

  # Handle country not found
  if type(originCountry) != type("A"):
    countries["NaN"] += 1
    continue

  if originCountry not in countries:
    countries[originCountry] = 1
    continue

  countries[originCountry] += 1
  index += 1



print("\rProgress - Done!")

# Sort countries by order of appearence
sorted = dict(sorted(countries.items(), reverse=True))
output = open("extracted/countryStats.json", "w")

# Save json output
jsonOutput = json.dumps(sorted, indent = 4)
output.write(jsonOutput)

# Print results on screen
for key in sorted:
  print("Number of IPs from", key, "-", countries[key])
