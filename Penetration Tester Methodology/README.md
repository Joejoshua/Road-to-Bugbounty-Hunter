# Penetration Tester Methodology

### Introduction to Penetration Testing
* **Penetration Tester:** A Pentester is a professional who tests the security of a system from an attacker's perspective.
* **Purpose:** To identify vulnerabilities that attackers might exploit and enhance the overall security of the system.
* **Common Targets:** Applications, Networks, and Hosts.
* **Relevant Environments:** On-premises, Cloud, and Hybrid.

---

### Methodology
* **Pentest Methodology:** A structured approach or guideline for conducting penetration tests.
* **Goals:** To evaluate system security and ensure the process is repeatable and systematic.
* **Benefits of Pentesting Methodology:** Ensures a structured workflow, establishes testing standards, and increases the credibility of the final report.

---

### Types of Methodology

* **OSSTMM (Open-Source Security Testing Methodology Manual):** Focused on Network Pentesting and Vulnerability Assessment.
* **OWASP (Open Worldwide Application Security Project):** Focused on Web, Mobile, API, and IoT Security.
* **PTES (Penetration Testing Execution Standard):** Divided into 7 main stages:
    - Pre-engagement Interactions
    - Intelligence Gathering
    - Threat Modeling
    - Vulnerability Analysis
    - Exploitation
    - Post Exploitation
    - Reporting

---

### Cyber Kill Chain

#### **CYCLE 1 (In Phase):** Attacker attempts to gain access to the target system or network
- **🔍 Reconnaissance:** Collecting public information about the target (OSINT).
- **🧰 Weaponisation:** Setting up infrastructure like C2 servers to manage the attack.
- **✉️ Delivery:** Sending the payload through various methods such as phishing or supply chain attacks.
- **🎭 Social Engineering:** Tricking victims into performing actions, such as clicking a link that appears to be from a trusted source.
- **💥 Exploitation:** Exploiting system or software vulnerabilities to execute the payload.
- **🔒 Persistence:** Establishing backdoors or maintaining access for future use.
- **🕵️ Defence Evasion:** Avoiding detection by disabling security mechanisms.
- **🌐 Command & Control (C2):** Connecting to the victim's machine over the internet to control it.
- **🔁 Loop:** If any step fails, the attacker may adapt or switch strategies to infiltrate the system.

#### **CYCLE 2 (Through Phase):** Attacker attempts to expand access and move within the network
- **🪜 Pivoting:** Using a compromised system as a base to attack other systems.
- **🔍 Discovery:** Gathering internal data like users, assets, and additional vulnerabilities.
- **🔓 Privilege Escalation:** Gaining higher-level permissions through exploits or misconfigurations.
- **💻 Execution:** Downloading and executing code to steal data or damage the system.
- **🔐 Credential Access:** Extracting account credentials from disk or memory.
- **🔄 Lateral Movement:** Using stolen credentials to access other systems within the network.

#### **CYCLE 3 (Out Phase):** Data theft, system damage, and evading detection
- **🔓 Collection:** 
    - Attacker discovers "data treasure troves."
    - Data collected may include trade secrets, financial data, and personal identifiable information (PII).
    - Impacts confidentiality.
- **📤 Exfiltration:** Stealing data from the system while avoiding detection.
- **💥 Impact:** 
    - Attack results in data integrity loss and system outages.
    - Consequences include financial loss and reputational damage.
- **🎯 Objectives:** 
    - Specific motives such as political agendas or business competition.

---
