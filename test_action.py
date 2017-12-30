import unittest
from action import Action

class ActionTest(unittest.TestCase):
    def setUp(self):
        self.testAction = Action()

    def test_ruleToString(self):
        self.assertEqual("001.txt",self.testAction.ruleToString("test.txt",1))

if __name__ == '__main__':
    unittest.main()