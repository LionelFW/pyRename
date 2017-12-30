import unittest
from rule import Rule

class RuleTest(unittest.TestCase):
    def setUp(self):
        self.testRule = Rule()

    #La classe est vide : pas de méthodes à tester dans Rule !
    #Le fichier est quand même là, c'est un "stub", au cas ou rule.py évoluerait

if __name__ == '__main__':
    unittest.main()