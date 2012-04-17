import unittest

from code.firstsecond import myfirst_yoursecond

class testFirstSecond(unittest.TestCase):
    def testPositive(self):
        self.assertTrue(myfirst_yoursecond("bell hooks", "curer bell"))

    def testNegative(self):
        self.assertFalse(myfirst_yoursecond("curer bell", "bell hooks"))

if __name__ == '__main__':
    unittest.main()
