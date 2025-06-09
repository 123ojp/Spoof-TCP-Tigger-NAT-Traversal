from scapy.all import IP, TCP, send
import argparse

def send_tcp_packet(src_ip, dst_ip, src_port, dst_port):
    ip = IP(src=src_ip, dst=dst_ip)
    tcp = TCP(sport=src_port, dport=dst_port, flags='S')  # SYN 封包
    packet = ip / tcp
    send(packet, verbose=0)
    print(f"Sent TCP packet from {src_ip}:{src_port} to {dst_ip}:{dst_port}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a TCP SYN packet with custom IP/port")
    parser.add_argument('-s', '--src_ip', required=True, help='Source IP address')
    parser.add_argument('-sp', '--src_port', type=int, required=True, help='Source port')
    parser.add_argument('-d', '--dst_ip', required=True, help='Destination IP address')
    parser.add_argument('-dp', '--dst_port', type=int, required=True, help='Destination port')
    args = parser.parse_args()

    send_tcp_packet(args.src_ip, args.dst_ip, args.src_port, args.dst_port)
