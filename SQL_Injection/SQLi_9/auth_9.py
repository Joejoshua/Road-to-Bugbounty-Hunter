#!/usr/bin/env python3

import requests, re, sys

username = sys.argv[1]
password = sys.argv[2]

URL = 'https://0af400cb04286b158042b7c7005700b0.web-security-academy.net/login'

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

you_are_admin = re.findall(r'<p>(Your username.*?)</p>', r.text)
if you_are_admin:
    print(f'[✓] {you_are_admin[0]}')