#!/usr/bin/env python3

import requests, re

username = "administrator"
password = "4905hsbr5ups3c2zfny0"

URL = 'https://0acf00c404298fdf81217a6300730064.web-security-academy.net/login'

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

admin= re.findall(r'<a href=(.*?)</a>', r.text)
print(admin)

# Step 3: Check result
if r.status_code == 500:
    print('[!] Internal Server Error!')