completeLog = open("extracted/failedPasswordAttempts.txt", "r").readlines()

ips = []
output = open("extracted/uniqueIPs.txt", "w")

for linha in completeLog:
  splitLine = linha.split()
  
  if   splitLine[9] == "user": ip = splitLine[12]
  elif splitLine[9] == "from": ip = splitLine[10]
  
  if ip not in ips:
    ips.append(ip)
    output.write(ip + "\n")
