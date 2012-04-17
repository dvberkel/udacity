import unittest

from code.fsm import fsmsim

class testInterpretation(unittest.TestCase):
    def setUp(self):
        self.edges = {(1,'q'): 1}
        self.accepting = [1]
        self.current = 1

    def testPositive(self):
        self.assertTrue(fsmsim('', self.current, self.edges, self.accepting))
        self.assertTrue(fsmsim('q', self.current, self.edges, self.accepting))
        self.assertTrue(fsmsim('qq', self.current, self.edges, self.accepting))
        self.assertTrue(fsmsim('qqq', self.current, self.edges, self.accepting))

    def testPositive(self):
        self.assertFalse(fsmsim('p', self.current, self.edges, self.accepting))

if __name__ == '__main__':
    unittest.main()
