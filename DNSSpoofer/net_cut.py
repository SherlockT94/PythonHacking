# netfilterqueue has some issues with pyhton3, so using python2 to run this script
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()#forward package
    packet.drop()#drop package

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)#process_packet is a function to handle every packet trapped
queue.run()

