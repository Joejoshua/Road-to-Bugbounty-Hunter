# Basic JavaScript Code

This section covers basic JavaScript syntax and concepts useful for beginners in penetration testing or web development.

## Variables

- `var`: Function-scoped. Can be **redeclared** and **updated**.
- `let`: Block-scoped. Can be **updated** but **not redeclared** in the same scope.
- `const`: Block-scoped. **Cannot be updated or redeclared**. Its value remains constant.

## Sample Code

```js
// Hello, World! program
console.log("Hello, World!");

// Variable and Data Type
let age = 25; // Number type

// Control Flow Statement
if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}

// Function
function greet(name) {
    console.log("Hello " + name + "!");
}

// Calling the function
greet("Bob");

// Prompt and Alert
let name = prompt("What is your name?"); // User input
alert("Hello " + name); // Alert message

// For Loop Example
for (let i = 0; i < 3; i++) {
    alert("Hacked");
}
```