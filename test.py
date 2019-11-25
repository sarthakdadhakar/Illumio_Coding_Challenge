# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:20:12 2019

@author: sarthak
"""

import unittest
from firewall import Firewall

class TestStringMethods(unittest.TestCase):
    
    def test_on_20_rules(self):
        """
        Testing on CSV of 20 rules
        """
        F = Firewall("firewall_rules.csv")
        self.assertEqual(True, F.accept_package("outbound", "udp", 30620, "131.132.159.67"))
        self.assertEqual(False, F.accept_package("outbound", "udp", 1005, "192.168.1.1"))
    
    def test_on_50k_rules(self):
        """
        Testing on CSV of 20 rules
        """
        F = Firewall("firewall_rules_50k.csv")
        self.assertEqual(True, F.accept_package("outbound", "tcp", 3322, "248.25.56.1"))
        self.assertEqual(False, F.accept_package("outbound", "udp", 65536, "10.168.1.1"))


if __name__ == '__main__':
    unittest.main()