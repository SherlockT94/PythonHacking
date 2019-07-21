# netfilterqueue has some issues with pyhton3, so using python2 to run this script
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())#convert packet to scapy packet
    if scapy_packet.haslayer(scapy.Raw):#Raw layer contain the http data
        print(scapy_packet.show())

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

