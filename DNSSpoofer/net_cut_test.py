import netfilterqueue

def packet_process(packet):
    print(packet)
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, packet_process)
queue.run()
