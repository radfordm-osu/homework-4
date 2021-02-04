import unittest
import hw4p1

class CubeTest(unittest.TestCase):
    def test_reg(self):
        result = hw4p1.CubeVolume(2, 2, 4)
        self.assertEqual(result, 16)

    def test_neg(self):
        result = hw4p1.CubeVolume(2, -2, 4)
        self.assertEqual(result, 16)

    def test_flt(self):
        result = hw4p1.CubeVolume(2, 2.5, 4.5)
        self.assertEqual(result, 22.5)

    if __name__ == "__main__":
        unittest.main()
