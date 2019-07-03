import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / Ip range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary())#Output: ARP who has Net(ip address) says your ip
    #scapy.ls(scapy.ARP())#list the field that we could set
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")#ff:ff:ff:ff:ff:ff is the broadcast MAC address(None)
    #print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request#combine them together
    #arp_request_broadcast.show()#show the details about this package
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]#srp -> sent n recieve package with a custom ether part, return two list with answered(index 0) and unanwered response

    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc} 
        clients_list.append(client_dict)
        #print(element[1].show())#element is couple of request and response(index 1)
        #print(element[1].psrc)
        #print(element[1].hwsrc)
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
        #print(clients_list)
        #print("-------------------------------------------")
    return clients_list
    
def print_result(clients_list):
    print("IP\t\t\tMACAddress")
    print("-------------------------------------------")
    for client in clients_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
