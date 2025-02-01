from scapy.all import Ether, sendp

def send_frame():
    frame = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast frame
    print("[Layer 1-2] Sending Ethernet frame...")
    sendp(frame, iface="eth0", verbose=False)

if __name__ == "__main__":
    send_frame()
