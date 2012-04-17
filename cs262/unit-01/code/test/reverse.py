import unittest

from code.fsm import fsmsim

class testReverseInterpretation(unittest.TestCase):
    def setUp(self):
        self.edges = {(1,'a'): 2,
                      (1,'b'): 3,  
                      (2,'c'): 4,
                      (3,'d'): 5,
                      (5,'c'): 2,
                      (5,'f'): 6,
                      (5,'g'): 1}
        self.accepting = [6]
        self.current = 1

    def testFMS(self):
        self.assertTrue(fsmsim('bdf', self.current, self.edges, self.accepting))
        self.assertTrue(fsmsim('bfgbdf', self.current, self.edges, self.accepting))

if __name__ == '__main__':
    unittest.main()
