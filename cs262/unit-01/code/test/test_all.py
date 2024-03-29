import unittest

from code.test.firstsecond import testFirstSecond
from code.test.regex import testRegex
from code.test.hyphenated import testHyphen
from code.test.function import testFunction
from code.test.escape import testEscape
from code.test.fsm import testFSM
from code.test.fsminterpretation import testInterpretation
from code.test.reverse import testReverseInterpretation

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testFirstSecond, 
                      testRegex, 
                      testHyphen, 
                      testFunction, 
                      testEscape, 
                      testFSM, 
                      testInterpretation,
                      testReverseInterpretation]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
