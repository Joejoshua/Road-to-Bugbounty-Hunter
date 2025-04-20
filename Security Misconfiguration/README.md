## ⚠️ Security Misconfiguration

Using a development version of PHP (`oldversion-dev`) in a production environment is a classic case of **Security Misconfiguration**.

> Development versions often include debugging features, insecure settings, or even intentional backdoors for testing purposes, and **should never be publicly accessible or used in production**.

In this project, the exposed development version led to **Remote Code Execution (RCE)** through a known backdoor exploit. This highlights the importance of:
- Disabling or removing dev environments before deployment.
- Keeping software updated with stable production releases.
- Regularly auditing configurations for security best practices.
