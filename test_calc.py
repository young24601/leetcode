import unittest
import sys
sys.path.insert(0, "d:\\documents\\github\\leetcode")
import calc2

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc2.add(1,2), 3)
        
if __name__ == '__main__':
    unittest.main()