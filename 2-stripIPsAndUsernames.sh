#!/bin/bash

# First, lets extract all relevant lines from log
mkdir extracted
chmod 600 extracted

echo "Unpacking logs..."
gunzip rawLogs/*.gz

cat rawLogs/* > extracted/completeLog.txt

echo "Extracting relevant part of logs..."
cat extracted/completeLog.txt | grep "Invalid user" > extracted/invalidUserLogs.txt
cat extracted/completeLog.txt | grep "Failed password for" > extracted/failedPasswordAttempts.txt

# extract unique IPs and usernames
echo -e "\nStarting IP stripping script..."
echo "###########"
python3 helperScripts/stripUniqueIPs.py
echo "###########"

echo -e "\nStarting Username stripping script..."
echo "###########"
python3 helperScripts/stripUniqueUsernames.py
echo "###########"
