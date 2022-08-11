completeLog = open("extracted/invalidUsers.txt", "r").readlines()

usernames = []
output = open("extracted/uniqueUsernames.txt", "w")

for linha in completeLog:
  user = linha.split()[7]
  
  if user not in usernames:
    usernames.append(user)
    output.write(user + "\n")
