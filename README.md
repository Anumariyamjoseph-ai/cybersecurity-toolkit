Cybersecurity Toolkit
A collection of small Python and Linux-based tools built to explore core cybersecurity concepts hands-on. Each tool focuses on a fundamental idea used in real-world security work.
Tools
1. Password Strength Checker
security-tools/password_checker.py
Analyzes a password and scores its strength based on length, character variety (uppercase, lowercase, numbers, symbols), and known weak/common passwords.

2. Port Scanner
security-tools/port_scanner.py
Wraps nmap to scan a target machine and report open network ports and running services — the same first step attackers and security auditors use to map out a system.
  
  
3. File Integrity Checker
security-tools/integrity_checker.py
Uses SHA-256 hashing to detect whether a file has been modified since it was last checked — the same principle behind antivirus tamper detection and file integrity monitoring (FIM) systems.
  

4. Log Analyzer
security-tools/log_analyzer.py
Scans a login log file and flags IP addresses with repeated failed login attempts, a common signature of brute-force attacks.
   
Why This Project
This toolkit was built to understand security concepts through direct, hands-on practice rather than theory alone — covering password security, network reconnaissance, tamper detection, and intrusion pattern recognition.
Tech Stack
Python 3
Linux command-line tools (nmap)
Built and tested entirely on a browser-based Linux environment (Replit)
