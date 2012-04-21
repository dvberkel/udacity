import unittest

from code.mind import nfsmaccepts

class testMind(unittest.TestCase):
    def setUp(self):
        self.edges = { (1, 'a') : [2,3],
                       (2, 'a') : [2],
                       (3, 'b') : [4, 2],
                       (4, 'c') : [5]}
        self.accepting = [5]

        self.edges2 = { (1, 'a') : [1],
                        (2, 'a') : [2]}
        self.accepting2 = [2]

    def testNfsmAccepts(self):
        self.assertFalse(nfsmaccepts(1, self.edges, self.accepting, []) == None)
        self.assertFalse(nfsmaccepts(1, self.edges, [4], []) == None)
        self.assertTrue(nfsmaccepts(1, self.edges2, self.accepting2, []) == None)
        self.assertFalse(nfsmaccepts(1, self.edges2, [1], []) == None)
    

if __name__ == '__main__':
    unittest.main()
