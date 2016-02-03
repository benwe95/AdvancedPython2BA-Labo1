# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3),6)
        self.assertEqual(utils.fact(4),24)
        #pour tester si la fonction lance une exception
        with self.assertRaises(ValueError):
            utils.fact(-1)
        
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,-2,1),(1.0))
        self.assertEqual(utils.roots(4,-4,1),(0.5))
    
    def test_integrate(self):
        self.assertTrue(15.8<utils.integrate('2*x',0,4),16<16.1)
        #Comme on APPROXIME l'intégrale, on ne pourra jamais obtenir la valeur exacte de -4/3
        self.assertTrue(-1.5<utils.integrate('x**2-1',-1,1)<-1.2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
