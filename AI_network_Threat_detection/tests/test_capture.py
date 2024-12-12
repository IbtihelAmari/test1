import unittest
import sys
sys.path.append(r'C:\Users\ibtihel\AI_network_Threat_detection\src')

from capture.interface_detection import detect_network_interfaces

class TestInterfaceDetection(unittest.TestCase):
    def test_detect_network_interfaces(self):
        interfaces = detect_network_interfaces()
        self.assertIsInstance(interfaces, list)

if __name__ == "__main__":
    unittest.main()
