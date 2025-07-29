# 🛡️ Penetration Testing Toolkit

A modular, multi-purpose penetration testing toolkit built with Python.  
Designed for ethical hackers, red teamers, and students learning cybersecurity.

---

## 🚀 Features

- 🔍 **Port Scanner** — Multi-threaded TCP port scanning
- 🔐 **SSH Brute-Force Attack** — Username + password list SSH login attempts
- ⚙️ **Modular Design** — Easy to extend and maintain

---

## 📁 Project Structure
 
penetration-toolkit/
│
├── toolkit.py # Main controller script
└── module/ # Toolkit modules
├── port_scanner.py # Port scanning module
└── brute_forcer.py # SSH brute-force module



---

## 🖥️ Requirements

- Python 3.8+
- Linux, macOS, WSL (Windows Subsystem for Linux), or native Windows (limited)
- SSH server running on target machine (for brute-force testing)

### 📦 Install Dependencies

```bash
pip install paramiko


Run the Toolkit
python .\toolkit.py  in windows

=== PENETRATION TESTING TOOLKIT ===
1. Port Scanner
2. Brute Force Attack
3. Exit


1. Port Scanner
Scans a range of TCP ports on a given target.

Example Input:
Enter target IP/hostname: 127.0.0.1
Enter start port: 20
Enter end port: 100


2. SSH Brute-Force
Attempts to log in via SSH using a wordlist of passwords.

Example Input:
Enter target IP: 127.0.0.1
Enter username: root
Enter path to password wordlist: passwords.txt

Sample passwords.txt:

123456
admin
test123
password

 
🛠️ SSH Server Setup (for Testing)
If testing locally in Linux or WSL:

Install & Start SSH Server
sudo apt update
sudo apt install openssh-server
sudo service ssh start

Enable Password Login (Optional)
Edit config:
sudo nano /etc/ssh/sshd_config

Ensure:
PermitRootLogin yes
PasswordAuthentication yes

Then restart SSH:
sudo systemctl restart ssh
