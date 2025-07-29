import socket
from concurrent.futures import ThreadPoolExecutor

def scan_ports(target, start, end):
    print(f"[+] Scanning {target} from port {start} to {end}...\n")

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"[OPEN] Port {port}")
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start, end + 1):
            executor.submit(scan_port, port)
