# Enterprise Software Security (ESS) Lab Programs

<p align="center">
  <img src="https://img.shields.io/github/stars/tharsan1305/ESS-REPO-?style=for-the-badge&color=gold" alt="GitHub Stars" />
  <img src="https://img.shields.io/github/forks/tharsan1305/ESS-REPO-?style=for-the-badge&color=blue" alt="GitHub Forks" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Kali_Linux-Ready-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Security-Lab-red?style=for-the-badge&logo=shield" alt="Security" />
</p>

---

<p align="center">
  ⭐ <b>If you find this repository helpful, please consider giving it a star!</b> ⭐
</p>

---

## 📑 Table of Contents

- [Repository Structure](#-repository-structure)
- [Lab Experiments Overview](#-lab-experiments-overview)
  - [01. SQL Injection Attack](#01-sql-injection-attack)
  - [02. Buffer Overflow Attack](#02-buffer-overflow-attack)
  - [03. Cross-Site Scripting (XSS)](#03-cross-site-scripting-xss)
  - [04. Web Application Penetration Testing](#04-web-application-penetration-testing)
  - [05. Secure Test Cases](#05-secure-test-cases)
  - [06. Penetration Testing Using Kali Linux](#06-penetration-testing-using-kali-linux)
- [Prerequisites & Environment](#-prerequisites--environment)
- [How to Run Each Program](#-how-to-run-each-program)
- [Concepts & Security Principles](#-concepts--security-principles)

---

## 📂 Repository Structure

```text
ESS-REPO-/
├── 01_SQL_Injection_Attack/
│   └── sql_injection.py               # Vulnerable vs Parameterized SQL queries
├── 02_Buffer_Overflow_Attack/
│   └── buffer_overflow.c              # Buffer overflow condition detection in C
├── 03_Cross_Site_Scripting_XSS/
│   └── xss_attack.py                  # Raw output vs HTML entity escaping in Python
├── 04_Web_Application_Penetration_Testing/
│   └── web_pentest.sh                 # Bash script for host discovery, HTTP headers & Nmap
├── 05_Secure_Test_Cases/
│   └── secure_test_cases.py           # Regex-based username & password validation suite
├── 06_Penetration_Testing_Using_Kali_Linux/
│   └── kali_pentest.py                # Cross-platform socket scanner & network auditing
└── README.md
```

---

## 🔬 Lab Experiments Overview

### 01. SQL Injection Attack
- **Folder:** `01_SQL_Injection_Attack/`
- **File:** `sql_injection.py`
- **Language:** Python (`sqlite3`)
- **Description:** Demonstrates an authentication bypass attack via dynamic query string concatenation using `' OR '1'='1`, and shows the secure mitigation using parameterized queries (prepared statements).

### 02. Buffer Overflow Attack
- **Folder:** `02_Buffer_Overflow_Attack/`
- **File:** `buffer_overflow.c`
- **Language:** C
- **Description:** Demonstrates stack buffer boundary checking. Detects when user input length exceeds the allocated memory buffer (`char buffer[10]`) to prevent memory corruption and unauthorized execution flow modification.

### 03. Cross-Site Scripting (XSS)
- **Folder:** `03_Cross_Site_Scripting_XSS/`
- **File:** `xss_attack.py`
- **Language:** Python
- **Description:** Illustrates the vulnerability of rendering raw, unescaped user input (e.g. `<script>alert('XSS')</script>`) and demonstrates the defense using `html.escape()` to sanitize input into safe HTML entities (`&lt;script&gt;`).

### 04. Web Application Penetration Testing
- **Folder:** `04_Web_Application_Penetration_Testing/`
- **File:** `web_pentest.sh`
- **Language:** Bash
- **Description:** Automates web application reconnaissance: fetches IP (`hostname -I`), OS details (`uname -a`), inspects HTTP response headers (`curl -I`), and performs Nmap port and service version scanning (`nmap -sV 127.0.0.1`).

### 05. Secure Test Cases
- **Folder:** `05_Secure_Test_Cases/`
- **File:** `secure_test_cases.py`
- **Language:** Python
- **Description:** Implements strict defensive input validation using regular expressions:
  - **Username Whitelist:** `^[A-Za-z0-9_]{3,15}$` (blocks metacharacters and ensures bounded length).
  - **Password Policy:** Minimum 8 characters, requiring at least one uppercase letter, one lowercase letter, and one digit.

### 06. Penetration Testing Using Kali Linux
- **Folder:** `06_Penetration_Testing_Using_Kali_Linux/`
- **File:** `kali_pentest.py`
- **Language:** Python
- **Description:** Performs network reconnaissance using low-level socket connections (`socket.connect_ex`) across standard ports (22, 80, 443, 8080) and inspects active listening sockets (`ss -tuln` on Linux / `netstat -ano` on Windows).

---

## 🛠 Prerequisites & Environment

- **Python:** 3.8+ (for Labs 01, 03, 05, 06)
- **C Compiler:** GCC / MinGW (for Lab 02)
- **Linux / Kali Linux:** Bash, `curl`, `nmap`, `apache2` (for Labs 04 & 06)

---

## 🚀 How to Run Each Program

### 🪟 Windows (PowerShell)

```powershell
# 01. SQL Injection Attack
python "01_SQL_Injection_Attack\sql_injection.py"

# 02. Buffer Overflow Attack (compile & run)
cd "02_Buffer_Overflow_Attack"
gcc buffer_overflow.c -o buffer_overflow.exe
.\buffer_overflow.exe
cd ..

# 03. Cross-Site Scripting (XSS)
python "03_Cross_Site_Scripting_XSS\xss_attack.py"

# 05. Secure Test Cases
python "05_Secure_Test_Cases\secure_test_cases.py"

# 06. Kali Linux Penetration Testing (Cross-platform)
python "06_Penetration_Testing_Using_Kali_Linux\kali_pentest.py"
```

### 🐧 Kali Linux Terminal

```bash
# 04. Web Application Penetration Testing
sudo systemctl start apache2
cd "04_Web_Application_Penetration_Testing"
chmod +x web_pentest.sh
./web_pentest.sh
cd ..

# 06. Penetration Testing
cd "06_Penetration_Testing_Using_Kali_Linux"
python3 kali_pentest.py
```

---

## 🛡 Concepts & Security Principles

| Lab | Threat / Vulnerability | Defensive Mechanism |
|:---:|:---|:---|
| **01** | SQL Injection (Authentication Bypass) | Parameterized Queries / Prepared Statements (`?`) |
| **02** | Buffer Overflow (Memory Corruption) | Input Boundary Checking (`strlen(input) >= sizeof(buffer)`) |
| **03** | Cross-Site Scripting (Client-Side Injection) | Context-Aware Output Encoding (`html.escape()`) |
| **04** | Exposed Web Headers & Unpatched Daemons | Security Header Hardening & Vulnerability Scanning (`curl`, `nmap`) |
| **05** | Malformed Input & Weak Credentials | Regex Whitelisting & Strong Password Policies |
| **06** | Unauthorized Listening Ports & Services | Active Socket Auditing & Network Attack Surface Mapping |

---

## 👤 Author
- **GitHub:** [@tharsan1305](https://github.com/tharsan1305)
- **Repository:** [ESS-REPO-](https://github.com/tharsan1305/ESS-REPO-.git)
