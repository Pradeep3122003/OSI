from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send

def send_packet():
    packet = IP(dst="127.0.0.1") / ICMP()
    print("[Layer 3] Sending IP packet...")
    send(packet, verbose=False)

if __name__ == "__main__":
    send_packet()
