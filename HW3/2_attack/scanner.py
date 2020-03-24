import sys
from collections import defaultdict
from socket import inet_ntoa

from dpkt.arp import ARP
from dpkt.compat import compat_ord
from dpkt.ethernet import Ethernet
from dpkt.ip import IP
from dpkt.pcap import Reader
from dpkt.tcp import TCP, TH_SYN
from dpkt.udp import UDP


def mac_addr(address):
    return ':'.join('%02x' % compat_ord(b) for b in address)


class ARPSpoofingChecker:
    static_arp = {
        '192.168.0.100': '7c:d1:c3:94:9e:b8',
        '192.168.0.103': 'd8:96:95:01:a5:c9',
        '192.168.0.1': 'f8:1a:67:cd:57:6e',
    }

    @staticmethod
    def is_valid(ip, mac):
        return ip not in ARPSpoofingChecker.static_arp or ARPSpoofingChecker.static_arp[ip] == mac

    @staticmethod
    def check(pkt_num, arp_pkt):
        src_ip = inet_ntoa(arp_pkt.spa)
        dst_ip = inet_ntoa(arp_pkt.tpa)

        src_mac = mac_addr(arp_pkt.sha)
        dst_mac = mac_addr(arp_pkt.tha)

        if not ARPSpoofingChecker.is_valid(src_ip, src_mac) or not ARPSpoofingChecker.is_valid(dst_ip, dst_mac):
            print(
                f"ARP spoofing!\n"
                f"Src MAC: {src_mac}\n"
                f"Dst MAC: {dst_mac}\n"
                f"Packet number: {pkt_num}"
            )


class PortScanChecker:
    def __init__(self):
        super().__init__()
        self.port_scan_dict = defaultdict(dict)

    def add(self, dst_ip, port, pkt_num):
        port_to_pkt_num = self.port_scan_dict[inet_ntoa(dst_ip)]
        if port not in port_to_pkt_num:
            port_to_pkt_num[port] = pkt_num

    def print(self):
        for (dst_ip, port_to_pkt_num) in self.port_scan_dict.items():
            if len(port_to_pkt_num) >= 100:
                pkt_nums = sorted(port_to_pkt_num.values())
                pkt_nums_str = ", ".join(map(str, pkt_nums))
                print(
                    f"Port scan!\n"
                    f"Dst IP: {dst_ip}\n"
                    f"Packet number: {pkt_nums_str}\n"
                )


def detect_arp(data):
    port_scan_checker = PortScanChecker()
    arp_spoofing_checker = ARPSpoofingChecker()

    for pkt_num, (_, pkt) in enumerate(data):
        eth_pkt = Ethernet(pkt)
        if isinstance(eth_pkt.data, ARP):
            arp_pkt = eth_pkt.data
            arp_spoofing_checker.check(pkt_num, arp_pkt)
        elif isinstance(eth_pkt.data, IP):
            ip_pkt = eth_pkt.data
            if isinstance(ip_pkt.data, TCP):
                tcp_pkt = ip_pkt.data
                if tcp_pkt.flags == TH_SYN:
                    port_scan_checker.add(ip_pkt.dst, tcp_pkt.dport, pkt_num)
            elif isinstance(ip_pkt.data, UDP):
                udp_pkt = ip_pkt.data
                port_scan_checker.add(ip_pkt.dst, udp_pkt.dport, pkt_num)

    port_scan_checker.print()


def main(filename):
    with open(filename, 'rb') as f:
        data = Reader(f)
        detect_arp(data)


if __name__ == '__main__':
    main(sys.argv[1])
