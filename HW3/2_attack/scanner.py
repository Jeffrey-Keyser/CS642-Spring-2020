import sys
from socket import inet_ntoa

from dpkt.arp import ARP
from dpkt.compat import compat_ord
from dpkt.ethernet import Ethernet
from dpkt.pcap import Reader


def mac_addr(address):
    return ':'.join('%02x' % compat_ord(b) for b in address)


def detect_arp(data):
    for (ts, buf) in data:
        eth_pkt = Ethernet(buf)
        ip_pkt = eth_pkt.data
        if isinstance(ip_pkt, ARP):
            print(inet_ntoa(ip_pkt.spa), inet_ntoa(ip_pkt.tpa), mac_addr(ip_pkt.sha), mac_addr(ip_pkt.tha))


def main(filename):
    with open(filename, 'rb') as f:
        data = Reader(f)
        detect_arp(data)


if __name__ == '__main__':
    main(sys.argv[1])
