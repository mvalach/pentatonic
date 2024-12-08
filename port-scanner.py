#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: port-scanner.py
Author: Michal Valach
Date: 2024-12-7
Description: Basic network port scanner


TODO:
- input validation
- exception handling
- more usefull output
- baner analysis integration
"""


import socket
import termcolor



def scan(target, ports):
        print("\n" + " Starting Scann For " + str(target))
        for port in range(1, ports+1):
                scan_port(target, port)

def scan_port(ipaddress, port):
        try:
                sock = socket.socket()
                sock.connect((ipaddress, port))
                print("[+] Port Opened " + str(port))
                sock.close()
        except:
                pass


targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports To Scan: "))

if ',' in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", "green"))
        for ip_addr in targets.split(','):
                scan(ip_addr.strip(' '), ports)
else:
        scan(targets, ports)