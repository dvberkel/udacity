import unittest
import re

from code.function import regexp

class testFunction(unittest.TestCase):
    def testPositive(self):
        self.assertEquals(["cos(0)"], re.findall(regexp, "cos(0)"))
        self.assertEquals(["sqrt(  2  )"], re.findall(regexp, "sqrt(  2  )"))

    def testNegative(self):
        self.assertNotEquals(["cos   (0)"], re.findall(regexp, "cos   (0)"))
        self.assertNotEquals(["sqrt(x)"], re.findall(regexp, "sqrt(x)"))

if __name__ == '__main__':
    unittest.main()
