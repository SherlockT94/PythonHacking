import subprocess 
import argparse 
import re

def getArguments(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address") 
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
    subprocess.call(["ifconfig", interface, "hw", "ether", newMAC])#hw for hardware
    subprocess.call(["ifconfig", interface, "up"])

def getCurrentMAC(interface):
    ifResult = subprocess.check_output(["ifconfig", interface])
    extractMAC = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifResult))
    if extractMAC:
        return extractMAC.group(0)
    else:
        print("[-] Could not read MAC Address.")

args = getArguments()
currentMAC = getCurrentMAC(args.interface)
print("Current MAC = " + str(currentMAC))

changeMAC(args.interface, args.newMAC)
currentMAC = getCurrentMAC(args.interface)
if currentMAC == args.newMAC:
    print("[+] MAC address was successfully changed to " + currentMAC)
else:
    print("[-] MAC address did not get changed MAC address did not get changed.")
