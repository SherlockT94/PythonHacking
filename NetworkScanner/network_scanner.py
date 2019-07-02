import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary())#Output: ARP who has Net(ip address) says your ip
    #scapy.ls(scapy.ARP())#list the field that we could set
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#ff:ff:ff:ff:ff:ff is the broadcast MAC address(None)
    #print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request#combine them together
    arp_request_broadcast.show()#show the details about this package

scan("10.0.2.1/24")
