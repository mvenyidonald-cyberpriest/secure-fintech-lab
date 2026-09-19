# secure-fintech-lab
This lab demonstrates how an attacker can take advantage of a vulnerability in a digital or financial system to gain unauthorized access, and harvest sensitive information for their selfish and malicious intent.
# Secure Fintech App Simulation - Cameroon Case Study
## Overview
Demonstration fo vsftp 2.3.4 vulnerability and secure coding fix for fintech context

## Lab Setup
-Attacker: Kali Linux (192.168.56.100/24)
-Victim: Metasploitable 2 (192.168.56.101/24)
-Network: Host-Only Adapter vboxnet0

## Tools Used
-Python3 + Scapy (recon.py)
-Nmap
Metasploit Framework

## Steps to Reproducce
1. Run recon on a kali terminal: 'sudo python3 scripts/recon.py'
2. Scan: 'nmap -sV -p 21, 80, 3306 192.168.56.101'
3. Exploit: 'msfconsole -q' -> 'use exploit/unix/ftp/vsftp_234_backdoor'

## Fix
See 'scripts/secure_app.py' - input validation, parameterized queries.

## Screenshots
See /screenshots folder for proof of root access.

## Disclaimer
For educational purposes only in isolated lab.


