import unittest
import lab1


class TestLab(unittest.TestCase):
    def test_value(self):
        self.assertEqual(lab1.ZeroCount(0), 1)
        self.assertEqual(lab1.ZeroCount(101), 1)
        self.assertEqual(lab1.ZeroCount(100), 2)

        
if __name__ == '__main__':
    unittest.main()
