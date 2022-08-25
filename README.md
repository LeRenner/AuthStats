# AuthStats
This script parses and generates statistics from failed authentication logs on Linux.

## Requirements

This script uses `python3` and the `iptocc` python library to parse IPs, usernames, and determine the countries of origin of the IP addresses. I recommend using [venv](https://docs.python.org/3/library/venv.html) for the installation of the library.

If you have python3 installed (and [pip](https://pip.pypa.io/en/stable/installation/)), you just need to run:

    pip install iptocc

to install iptocc.

## How to parse your logs

This repository contains 3 scripts. Here's a breakdown of their purposes

### 1-requiresSudo.sh

This script should be run as your user and requires sudo permission. It creates a folder called `extracted`, copies all authentication logs to it, and changes their permission to be accessible to your user.

If you would rather do this step manually, just create a folder called `extracted` in the root of this repository, and copy all `auth*.log` files from (usually) the `/var/log/` directory into it. Then just change the permissions so these files are accessible for your user.

### 2-stripIPsAndUsernames.sh

This script extracts all unique usernames and origin IPs from failed login attempts. Files are created in the extracted directory.

### 3-queryCountries.sh

This script queries the countries of origin from the IP addresses, and created a file in the `extracted` folder with the number of IPs from each country.
