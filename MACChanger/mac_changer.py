import subprocess
import argparse

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interfacef to change its MAC address")
    parser.add_argument("-m", "--mac", dest="newMAC", help="New MAC Address")
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if not args.newMAC:
        parser.error("[-] Please specify an new MAC address, use --help for more info")
    return args

def changeMAC(interface, newMAC):
    print("[+] Changing MAC address for " + interface + " to " + newMAC)
    subprocess.call(["ifconfig", interface, "down"])#for security reason, use + to concatenate String may cause code injection
    subprocess.call(["ifconfig", interface, "hw", "ether", newMAC])
    subprocess.call(["ifconfig", interface, "up"])

args = getArguments()
changeMAC(args.interface, args.newMAC)
