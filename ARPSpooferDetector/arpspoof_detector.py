import scapy.all as scapy
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request#combine them together
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]#srp -> sent n recieve package with a custom ether part, return two list with answered(index 0) and unanwered response
    return answered_list[0][1].hwsrc

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)#prn: print - mean if find something interesting, display it

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print("[+] You are under ARP Spoofing attack!!!")
        except IndexError: #if the dst field is the ip of this machine, it will raise IndexError 
            pass

sniff("eth0")
