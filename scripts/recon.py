from scapy.all import ARP, Ether, srp

# Change to your lab range
target_ip = "192.168.56.100/24"

# Create ARP request packet
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

print(f"[+] Scanning {target_ip} for live hosts...")

result = srp(packet, timeout=3, verbose=0)[0]

print("Available Hosts:")
print("IP" + " "*18 +"MAC")
for sent, received in result:
        print(f"{received.psrc:20s} {received.hwsrc}")

