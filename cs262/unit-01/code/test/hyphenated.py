import unittest
import re

from code.hyphenated import regexp

class testHyphen(unittest.TestCase):
    def testPositive(self):
        self.assertEquals(["well-liked"], re.findall(regexp, "well-liked"))
        self.assertEquals(["html"], re.findall(regexp, "html"))

    def testNegative(self):
        self.assertNotEquals(["a-b-c"], re.findall(regexp, "a-b-c"))
        self.assertNotEquals(["a--b"], re.findall(regexp, "a--b"))

if __name__ == '__main__':
    unittest.main()
