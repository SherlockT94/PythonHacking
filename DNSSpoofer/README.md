# How to use it
start apache server

echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -I FORWARD -j NFQUEUE --gueue-num 0

run ARP Spoofer
run the script

test on nat network successfully.
# How to start Apache server
service apache2 start

