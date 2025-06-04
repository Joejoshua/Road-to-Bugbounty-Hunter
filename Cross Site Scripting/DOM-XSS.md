# DOM XSS

DOM XSS occurs when malicious code from the client-side (user input) is inserted into the Document Object Model (DOM) without being sent to the server and without proper sanitization.

---

## Test Basic DOM Manipulation

#### Step 1: Insert Sample HTML

Paste the following HTML into your browser's **Elements** tab in DevTools:

```html
<p id="demo">Original Text</p>
```

#### Step 2: Modify Content via JavaScript

Paste the following JavaScript into the Console tab:

```js
let paragraph = document.getElementById("demo");
paragraph.innerHTML = "Javascript is powerful!";
```

The text inside the `<p id="demo">` will change from `Original Text` to `Javascript is powerful!`.

---

### Change to XSS

By inserting unsanitized user input, we can simulate a DOM XSS vulnerability:

```js
let userInput = "<img src=x onerror=alert('xss')>";
paragraph.innerHTML = userInput; // XSS vulnerability if input is not sanitized
```

This will inject an image tag that triggers `alert('xss')` when the browser encounters an error loading the image, showing a real example of client-side XSS.

---

### Using querySelector Safely

#### Step 1: Insert Button HTML

Paste the following into the Elements tab:

```html
<button id="myButton">Original</button>
```

#### Step 2: JavaScript Behavior

Paste this into the Console tab:

```js
let container = document.querySelector("#myButton");
container.innerText = `<button id="myButton" onclick="alert(1)">Click me</button>`;
```

- Explanation:
    - `innerText` renders HTML as plain text, so no script execution occurs.
    - If we used `innerHTML` instead, the code would be interpreted and potentially executed, leading to XSS if input is malicious and unsanitized.

---

### Advanced Example: Using `eval()`

```js
let maliciousCode = "alert('XSS via eval!')";
eval(maliciousCode); // Dangerous: executes any string as code!
```

Using `eval()` on user-controlled input is extremely dangerous and a common vector for DOM XSS.