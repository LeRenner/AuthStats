import sys

print("Opening file...")
completeLog = open("extracted/invalidUserLogs.txt", "r").readlines()

usernames = []
output = open("extracted/uniqueUsernames.txt", "w")
index = 0


for linha in completeLog:

  # update progress every 2000 lines
  if index % 2000 == 0:
    sys.stdout.write("\rProgress - %s%%" % str(round(100 * index/len(completeLog), 2)))
    sys.stdout.flush()

  # consider empty username case
  if "user  " in linha: continue

  user = linha.split()[7]

  if user not in usernames:
    usernames.append(user)
    output.write(user + "\n")

  index += 1


print("\rProgress - Done!")
