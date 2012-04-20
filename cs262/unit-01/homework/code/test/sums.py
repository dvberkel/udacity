import unittest

from code.sums import sumnums

class testSums(unittest.TestCase):
    def testSums(self):
        input = """he Act of Independence of Lithuania was signed 
on February 16, 1918, by 20 council members."""
        
        self.assertEquals(1954, sumnums(input))

if __name__ == '__main__':
    unittest.main()
