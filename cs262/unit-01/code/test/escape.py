import unittest
import re

from code.escape import regexp

class testEscape(unittest.TestCase):
    def testPositive(self):
        self.assertEquals(['"I say \\"Hello\\""'], re.findall(regexp, '"I say \\"Hello\\""'))

    def testNegative(self):
        self.assertNotEquals(['"\\"'], re.findall(regexp, '"\\"'))

if __name__ == '__main__':
    unittest.main()
