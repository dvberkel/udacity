import unittest

from code.test.sums import testSums
from code.test.nfsm import testNFSM
from code.test.mind import testMind

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testSums, testNFSM, testMind]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
