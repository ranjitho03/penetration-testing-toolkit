import sys
from module import port_scanner, brute_forcer

def main():
    while True:
        print("\n=== PENETRATION TESTING TOOLKIT ===")
        print("1. Port Scanner")
        print("2. Brute Force Attack")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            target = input("Enter target IP/hostname: ")
            start = int(input("Enter start port: "))
            end = int(input("Enter end port: "))
            port_scanner.scan_ports(target, start, end)

        elif choice == '2':
            target = input("Enter target IP: ")
            username = input("Enter username: ")
            wordlist = input("Enter path to password wordlist: ")
            brute_forcer.brute_force(target, username, wordlist)

        elif choice == '3':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
