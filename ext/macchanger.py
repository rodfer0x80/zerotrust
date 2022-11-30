#!/usr/bin/python3


import subprocess
import random
import sys
import re
import os


class MACX:
    def __init__(self, interface="wlan0"):
        self.interface = interface
        self.ifconfig_result = ""
        self.perm_mac = self.get_current_mac()
        self.new_mac = self.generate_new_mac()
        return None

    def get_current_mac(self):
        self.ifconfig_result = subprocess.check_output(
            ["ifconfig", self.interface])
        mac_address_search_result = re.search(
            r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))
        if mac_address_search_result:
            sys.stdout.write(
                f"[+] Found current MAC address: {mac_address_search_result} (get_current_mac)\n")
            return mac_address_search_result.group(0)
        else:
            sys.stderr.write(
                "[x] Could not read MAC address (get_current_mac)\n")
        return None

    def change_mac(self):
        sys.stdout.write(
            f"[*] Changing MAC address for {interface} to {new_mac} \n")
        subprocess.call(["ifconfig", self.interface, "down"])
        subprocess.call(["ifconfig", self.interface,
                        "hw", "ether", self.new_mac])
        subprocess.call(["ifconfig", self.interface, "up"])
        sys.stdout.write(
            f"[*] Permanent MAC address: {perm_mac} (change_mac)\n")
        sys.stdout.write(f"[+] New MAC address: {new_mac} (change_mac)\n")
        sys.stdout.write("[*] Result from ifconfig command (change_mac)\n")
        subprocess.call(["ifconfig", self.interface, "|", "grep", "ether"])
        return None

    def generate_new_mac(self):
        new_mac = input(
            "Enter new MAC address or ENTER to randomly generate:\n>>> ")
        if new_mac == "":
            alphabet = "0123456789abcdef"
            mac_size = 12 // 2
            sep = ":"
            new_mac = ""
            for i in range(mac_size):
                char1 = random.choice(alphabet)
                char2 = random.choice(alphabet)
                new_mac += f"{char1}{char2}:"
            new_mac = new_mac[:len(new_mac)-1]
        else:
            if re.fullmatch(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", new_mac) == None:
                print("[x] Error format for new MAC address entered")
                sys.exit(2)
                generate_new_mac()
        return new_mac


if __name__ == '__main__':
    if os.geteuid() != 0:
        sys.stderr.write("Error: program must be run with ID 0\n")
        sys.exit(1)
    interface = input(
        "Enter interface name or ENTER for default value wlan0\n>>> ")
    if interface == "":
        interface = "wlan0"
    macx = MACX()
    macx.change_mac()
