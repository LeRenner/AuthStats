# First, lets extract all relevant lines from log
mkdir extracted

gunzip rawLogs/*.gz

cat rawLogs/* > extracted/completeLog.txt

cat extracted/completeLog.txt | grep "Invalid user" > extracted/invalidUserLogs.txt
cat extracted/completeLog.txt | grep "Failed password for" > extracted/failedPasswordAttempts.txt

# extract unique IPs and usernames
python3 helperScripts/stripUniqueIPs.py
python3 helperScripts/stripUniqueUsernames.py
