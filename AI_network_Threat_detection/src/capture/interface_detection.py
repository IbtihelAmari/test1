import psutil

def detect_network_interfaces():
    print("Détection des interfaces réseau disponibles...")
    interfaces = psutil.net_if_addrs()
    valid_interfaces = [iface for iface in interfaces if 'Ethernet' in iface or 'Wi-Fi' in iface]
    if valid_interfaces:
        print("Interfaces disponibles :", valid_interfaces)
        return valid_interfaces
    else:
        print("Aucune interface Wi-Fi ou Ethernet disponible.")
        return []
