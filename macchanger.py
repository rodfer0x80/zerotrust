import subprocess
import random
import re


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[x] Could not read MAC address")


def change_mac(interface, perm_mac, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(f"[*] Permanent MAC address: {perm_mac}")
    print(f"[*] New MAC address: {new_mac}")
    print("Result from ifconfig command")
    subprocess.call(["ifconfig", interface, "|", "grep", "ether"])


def generate_new_mac():
    new_mac = input("Enter new MAC address or ENTER to randomly generate:\n>>> ")
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
            exit(0)
            generate_new_mac()
    return new_mac

if __name__ == '__main__':
    interface = input("Enter interface name or ENTER for default value wlan0\n>>> ")
    perm_mac = get_current_mac(interface)
    new_mac = generate_new_mac()
    change_mac(interface, perm_mac, new_mac)
