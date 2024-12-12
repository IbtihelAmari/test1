import sys
import os

# Ajouter la racine 'src' au PYTHONPATH
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if src_path not in sys.path:
    sys.path.append(src_path)

# Afficher les chemins de recherche pour vérification
print("C:/Users/ibtihel/AI_network_Threat_detection/src/capture:", sys.path)

# Importer le module
from capture.interface_detection import detect_network_interfaces
print("Import réussi !")
def select_network_interface():
    interfaces = detect_network_interfaces()
    if not interfaces:
        print("Aucune interface détectée. Terminé.")
        return None

    print("Veuillez sélectionner une interface :")
    for idx, iface in enumerate(interfaces):
        print(f"{idx + 1}. {iface}")

    try:
        choice = int(input("Entrez le numéro de l'interface : ")) - 1
        if 0 <= choice < len(interfaces):
            print(f"Interface sélectionnée : {interfaces[choice]}")
            return interfaces[choice]
        else:
            print("Sélection invalide.")
    except ValueError:
        print("Entrée invalide.")
    return None
