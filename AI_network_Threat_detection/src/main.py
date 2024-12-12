from capture.interface_selection import select_network_interface
from capture.packet_capture import capture_packets, capture_on_multiple_interfaces

def main():
    print("Bienvenue dans le système de capture réseau.")
    selected_interface = select_network_interface()
    if selected_interface:
        print("Capture sur une seule interface sélectionnée...")
        capture_packets(selected_interface)

        # Exemple pour la capture multi-interface
        print("Capture sur plusieurs interfaces...")
        capture_on_multiple_interfaces([selected_interface])

if __name__ == "__main__":
    main()
