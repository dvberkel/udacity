import unittest
import re

from code.regex import regexp

class testRegex(unittest.TestCase):
    def testPositive(self):
        self.assertEquals(["ab"], re.findall(regexp, "ab"))
        self.assertEquals(["1"], re.findall(regexp, "1"))
        self.assertEquals(["123"], re.findall(regexp, "123"))

    def testNegative(self):
        self.assertNotEquals(["a"], re.findall(regexp, "a"))
        self.assertNotEquals(["abc"], re.findall(regexp, "abc"))

if __name__ == '__main__':
    unittest.main()
