import unittest
import sys
from ruleset import Ruleset

class RulesetTest(unittest.TestCase):
    def setUp(self):
        self.rsTest = Ruleset()

    def test_load(self):
        self.assertTrue(self.rsTest.load())
        self.assertFalse(self.rsTest.load("fichierinexistant.ini"))
    
    def test_save(self):
        self.assertTrue(self.rsTest.save())
        self.assertTrue(self.rsTest.save("test.ini"))

if __name__ == '__main__':
    unittest.main()