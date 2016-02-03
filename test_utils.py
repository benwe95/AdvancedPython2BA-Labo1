# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3),6)
        self.assertEqual(utils.fact(4),24)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,-2,1),(1))
        self.assertEqual(utils.roots(4,1,-4),(0.5))
    
    def test_integrate(self):
        self.assertEqual(utils.integrate(2*x,0,4),8)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
