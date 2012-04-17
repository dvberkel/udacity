import unittest

from code.fsm import fsmsim

class testFSM(unittest.TestCase):
    def setUp(self):
        self.edges = {(1,'a'): 2,
                      (2,'a'): 2,
                      (2,'1'): 3,
                      (3,'1'): 3}
        self.accepting = [3]
        self.current = 1

    def testFMS(self):
        self.assertTrue(fsmsim('aa111', self.current, self.edges, self.accepting))

if __name__ == '__main__':
    unittest.main()
