# Web Security Assessment Dashboard

A Flask-based automated vulnerability assessment platform designed to perform reconnaissance, web security scanning, and basic vulnerability analysis through a centralized dashboard interface.

---

# Project Overview

The **Web Security Assessment Dashboard** is a cybersecurity-focused web application that integrates multiple security tools into a single platform.

The project automates the process of:

- Port Scanning
- Web Vulnerability Scanning
- CMS Enumeration
- SQL Injection Testing
- XSS Simulation
- Security Report Generation

The platform provides a real-time scanning interface, downloadable reports, and a hacker-themed dashboard UI inspired by professional security tools.

---

# Objectives

- Automate basic penetration testing workflows
- Learn real-world vulnerability assessment concepts
- Integrate multiple security tools into one interface
- Build hands-on experience with Flask and Python automation
- Create a practical cybersecurity portfolio project

---

# Features

## Real-Time Scan Output

Displays scan results live while tools are running.

---

##  Tool Selection System

Users can select specific tools before starting the scan.

### Supported Tools

- Nmap
- Nikto
- Nuclei
- WPScan
- SQLMap

---

##  Port Scanning

Uses Nmap for network reconnaissance and service detection.

### Example

```bash
nmap -p 21,22,80,443 target
```

---

##  Nikto Integration

Performs web server vulnerability scanning.

### Detects

- Dangerous files
- Outdated software
- Security misconfigurations
- Missing headers

---

##  Nuclei Integration

Performs template-based vulnerability scanning.

### Detects

- CVEs
- Misconfigurations
- Exposed panels
- Known vulnerabilities

---

##  WPScan Integration

Optional WordPress vulnerability scanning.

### Features

- User Enumeration
- Plugin Enumeration
- Theme Enumeration

---

##  SQLMap Integration

Tests web applications for SQL Injection vulnerabilities.

### Example Detection

```text
Parameter 'id' appears vulnerable to SQL injection
```

---

##  XSS Simulation

Performs basic reflected XSS payload simulation.

### Example Payload

```html
<script>alert('XSS')</script>
```

---

##  Downloadable Reports

Users can download generated scan reports after completion.

### Generated Format

```text
security_scan_report.txt
```

---

##  Hacker-Themed UI

Custom cybersecurity-inspired interface using:

- Dark terminal theme
- Green hacker colors
- Animated loading spinner
- Live output console

---

#  Project Workflow

##  Complete Working Flow

```text
User Input
    ↓
Flask Backend
    ↓
Selected Security Tools
    ↓
Scan Execution
    ↓
Real-Time Output Streaming
    ↓
Report Generation
    ↓
Downloadable Results
```

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Flask | Web framework |
| HTML/CSS/JavaScript | Frontend UI |
| Nmap | Port scanning |
| Nikto | Web server scanning |
| Nuclei | Vulnerability scanning |
| WPScan | WordPress scanning |
| SQLMap | SQL Injection testing |

---

#  Project Structure

```text
website-security-dashboard/
│
├── app.py
├── scanner.py
├── requirements.txt
├── README.md
│
├── reports/
│   └── latest_scan_report.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

#  Installation Guide

## 1️ Clone Repository

```bash
git clone https://github.com/yourusername/web-security-assessment-dashboard.git

cd web-security-assessment-dashboard
```

---

## 2️ Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

##  Install Required Security Tools

### Nmap

```bash
sudo apt install nmap
```

### Nikto

```bash
sudo apt install nikto
```

### Nuclei

```bash
sudo apt install nuclei
```

### SQLMap

```bash
sudo apt install sqlmap
```

### WPScan

```bash
sudo apt install wpscan
```

---

#  Running the Application

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

#  Safe Testing Targets

## Vulnerable Test Website

```text
http://testphp.vulnweb.com
```

## WordPress Testing

```text
https://wptest.io
```

## Nmap Official Test Host

```text
scanme.nmap.org
```

---

#  Example Scan Report

```text
==============================
Website Security Scan Report
==============================

Target: testphp.vulnweb.com
Date: 2026-04-30

=== Nmap Scan ===
Port 80 Open
Port 443 Open

=== Nikto Scan ===
Missing Security Headers

=== SQLMap ===
Possible SQL Injection Detected
```

---

#  Ethical Usage Notice

This project is intended only for educational purposes and authorized security testing.

## Do NOT Scan

- Government systems
- Banking websites
- Production servers
- Unauthorized targets

Always obtain proper permission before performing security assessments.

---

#  Future Improvements

- Vulnerability Severity Classification
- PDF Report Generation
- OWASP Top 10 Mapping
- Scan History Database
- User Authentication
- Multi-Target Scanning
- Background Scanning
- Uptime Monitoring
- Email / Telegram Alerts
- Dashboard Analytics

---

#  Learning Outcomes

This project helped in understanding:

- Web application security
- Vulnerability assessment workflows
- Python automation
- Flask backend development
- Security tool integration
- Real-time frontend communication
- Report generation systems

---

#  Resume Description

```text
Developed a Flask-based Web Security Assessment Dashboard integrating Nmap, Nikto, Nuclei, WPScan, and SQLMap with live scan streaming, customizable tool selection, and downloadable security reports.
```

---

#  Author

## Ayush Sharma

Cybersecurity Enthusiast | System & Network Administration 

### GitHub

```text
https://github.com/ayushx69
```

### LinkedIn

```text
https://linkedin.com/in/ayushx69
```

---

#  Final Notes

This project was built to combine multiple cybersecurity tools into a centralized dashboard for learning and practicing vulnerability assessment concepts in a safe and interactive environment.
