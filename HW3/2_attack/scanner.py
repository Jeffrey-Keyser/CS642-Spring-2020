import sys
from collections import defaultdict
from socket import inet_ntoa, inet_aton

from dpkt.arp import ARP
from dpkt.compat import compat_ord
from dpkt.ethernet import Ethernet
from dpkt.ip import IP
from dpkt.pcap import Reader
from dpkt.tcp import TCP, TH_SYN
from dpkt.udp import UDP


def mac_ntoa(mac_bytes):
    return ':'.join('%02x' % compat_ord(b) for b in mac_bytes)


def mac_aton(mac_str):
    return bytes.fromhex(mac_str.replace(":", ""))


static_arp = {
    inet_aton('192.168.0.100'): mac_aton('7c:d1:c3:94:9e:b8'),
    inet_aton('192.168.0.103'): mac_aton('d8:96:95:01:a5:c9'),
    inet_aton('192.168.0.1'): mac_aton('f8:1a:67:cd:57:6e'),
}


def check_arp_spoofing(pkt_num, arp_pkt):
    src_ip = arp_pkt.spa
    src_mac = arp_pkt.sha
    dst_mac = arp_pkt.tha

    if src_ip in static_arp and static_arp[src_ip] != src_mac:
        print(
            f"ARP spoofing!\n"
            f"Src MAC: {mac_ntoa(src_mac)}\n"
            f"Dst MAC: {mac_ntoa(dst_mac)}\n"
            f"Packet number: {pkt_num}"
        )


class PortScanDetector:
    def __init__(self):
        super().__init__()
        self.ip_to_port_data = defaultdict(dict)

    def add(self, pkt_num, ip_pkt):
        port_to_pkt_num = self.ip_to_port_data[ip_pkt.dst]
        port = ip_pkt.data.dport
        if port not in port_to_pkt_num:
            port_to_pkt_num[port] = pkt_num

    def print(self):
        for (dst_ip, port_to_pkt_num) in self.ip_to_port_data.items():
            if len(port_to_pkt_num) >= 100:
                pkt_nums = sorted(port_to_pkt_num.values())
                pkt_nums_str = ", ".join(map(str, pkt_nums))
                print(
                    f"Port scan!\n"
                    f"Dst IP: {inet_ntoa(dst_ip)}\n"
                    f"Packet number: {pkt_nums_str}\n"
                )


class SYNFloodDetector:
    def __init__(self):
        super().__init__()
        self.ip_port_to_pkts = defaultdict(list)

    def check(self, pkt_num, ts, ip_pkt):
        ip = ip_pkt.dst
        port = ip_pkt.data.dport
        pkt_list = self.ip_port_to_pkts[(ip, port)]

        pkt_list.append((ts, pkt_num))

        if len(pkt_list) < 101:
            pkt_list[:] = [e for e in pkt_list if ts - e[0] < 1]
        else:
            pkt_nums = sorted(pkt_num for (_, pkt_num) in pkt_list)
            pkt_nums_str = ", ".join(map(str, pkt_nums))
            print(
                f"SYN floods!\n"
                f"Dst IP: {inet_ntoa(ip)}\n"
                f"Dst Port: {port}\n"
                f"Packet number: {pkt_nums_str}\n"
            )
            pkt_list.clear()


def detect(data):
    port_scan_detector = PortScanDetector()
    syn_flood_detector = SYNFloodDetector()

    for pkt_num, (ts, pkt) in enumerate(data):
        eth_pkt = Ethernet(pkt)
        if isinstance(eth_pkt.data, ARP):
            arp_pkt = eth_pkt.data
            check_arp_spoofing(pkt_num, arp_pkt)
        elif isinstance(eth_pkt.data, IP):
            ip_pkt = eth_pkt.data
            if isinstance(ip_pkt.data, TCP):
                if ip_pkt.data.flags & TH_SYN:
                    port_scan_detector.add(pkt_num, ip_pkt)
                    syn_flood_detector.check(pkt_num, ts, ip_pkt)
            elif isinstance(ip_pkt.data, UDP):
                port_scan_detector.add(pkt_num, ip_pkt)

    port_scan_detector.print()


def main(filename):
    with open(filename, 'rb') as f:
        data = Reader(f)
        detect(data)


if __name__ == '__main__':
    main(sys.argv[1])
