import sys

print("Opening file...")
completeLog = open("extracted/failedPasswordAttempts.txt", "r").readlines()

ips = []
output = open("extracted/uniqueIPs.txt", "w")

print("Processing...")
index = 0

for linha in completeLog:

  # update progress every 2000 lines
  if index % 2000 == 0:
    sys.stdout.write("\rProgress - %s%%" % str(round(100* index/len(completeLog), 2)))
    sys.stdout.flush()

  splitLine = linha.split()

  if   splitLine[9] == "user": ip = splitLine[12]
  elif splitLine[9] == "from": ip = splitLine[10]

  if ip not in ips:
    ips.append(ip)
    output.write(ip + "\n")

  index += 1

print("\rProgress - Done!")
