import unittest
from main import inventory

XML = '<nmaprun><host><status state="up"/><address addr="192.0.2.10" addrtype="ipv4"/><ports><port protocol="tcp" portid="22"><state state="open"/><service name="ssh"/></port><port protocol="tcp" portid="80"><state state="closed"/></port></ports></host></nmaprun>'


class InventoryTests(unittest.TestCase):
    def test_only_open_ports(self):
        result = inventory(XML)
        self.assertEqual(result[0]["addresses"]["ipv4"], "192.0.2.10")
        self.assertEqual(result[0]["open_ports"], [{"port": 22, "protocol": "tcp", "service": "ssh"}])


if __name__ == "__main__":
    unittest.main()
