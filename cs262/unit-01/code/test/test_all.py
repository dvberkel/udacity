import unittest

from code.test.firstsecond import testFirstSecond
from code.test.regex import testRegex
from code.test.hyphenated import testHyphen

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testFirstSecond, testRegex, testHyphen]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
