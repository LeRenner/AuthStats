#!/usr/bin/python3

import sys
import iptocc
import logging
import json

index = 0
ips = open("extracted/uniqueIPs.txt", "r", encoding="utf-8").readlines()
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
        sys.stdout.write(f"\rProgress - {round(100 * index/len(ips), 2)}")
        sys.stdout.flush()

    # Handle invalid IP address
    originCountry = 0
    try:
        originCountry = iptocc.get_country_code(ip[:-1])
    except:
        print(f"Country code not found for {ip[:-1]}.")

    # Handle country not found
    if not isinstance(originCountry, str):
        countries["NaN"] += 1
        continue

    if originCountry not in countries:
        countries[originCountry] = 1
        continue

    countries[originCountry] += 1
    index += 1

print("\rProgress - Done!")

# Sort countries by order of appearance
sorted_dict = dict(sorted(countries.items(), reverse=True))
output = open("extracted/countryStats.json", "w", encoding="utf-8")

# Save json output
jsonOutput = json.dumps(sorted_dict, indent=4)
output.write(jsonOutput)

# Print results on screen
for key in sorted_dict:
    print(f"Number of IPs from {key} - {countries[key]}")
