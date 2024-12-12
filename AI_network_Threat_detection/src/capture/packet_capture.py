from scapy.all import sniff

def capture_packets(interface, packet_count=10):
    print(f"Capture des paquets sur l'interface {interface}...")
    packets = sniff(iface=interface, count=packet_count, prn=lambda x: x.summary())
    print(f"{len(packets)} paquets capturés.")
    return packets

def capture_on_multiple_interfaces(interfaces):
    from multiprocessing import Process

    processes = []
    for interface in interfaces:
        p = Process(target=capture_packets, args=(interface, 10))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
