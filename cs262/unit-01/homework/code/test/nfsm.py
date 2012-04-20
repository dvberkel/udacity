import unittest

from code.nfsm import nfsmsim

class testNFSM(unittest.TestCase):
    def setUp(self):
        self.edges = { (1, 'a') : [2, 3],
                       (2, 'a') : [2],
                       (3, 'b') : [4, 3],
                       (4, 'c') : [5] }
        self.accepting = [2,5]

    def testPositive(self):
        self.assertTrue(nfsmsim("abc", 1, self.edges, self.accepting))
        self.assertTrue(nfsmsim("aaa", 1, self.edges, self.accepting))
        self.assertTrue(nfsmsim("abbbc", 1, self.edges, self.accepting))
    
    def testNegative(self):
        self.assertFalse(nfsmsim("aabc", 1, self.edges, self.accepting))
        self.assertFalse(nfsmsim("", 1, self.edges, self.accepting))

if __name__ == '__main__':
    unittest.main()
