# How to use it
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -I FORWARD -j NFQUEUE --gueue-num 0

run ARP Spoofer
python replace_downloads.py

test on nat network successfully.
