#!/usr/bin/python3
import scapy.all as scapy
import argparse


DESTINATION = "ff:ff:ff:ff:ff:ff"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", action="store", help="Please specify target IP address or range")
    return parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=DESTINATION)
    arp_request_broadcast = broadcast/arp_request
    # using srp insted of sr because of custom ether
    answerred, _ = scapy.srp(arp_request_broadcast, timeout=1)
    
    clients = []
    for element in answerred:
        clients.append({
            "ip": element[1].psrc,
            "mac": element[1].hwsrc,
    })

    return clients

def output_results(clients):
    print("\nIP Address\t\t MAC Address")
    print("------------------------------------------")
    for client in clients:
        print(client["ip"], "\t\t", client["mac"])
        
if __name__ == "__main__":
    arguments = get_arguments()
    results = scan(arguments.target)
    output_results(results)
