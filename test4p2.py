import unittest
import hw4p2

class ListTest(unittest.TestCase):
    def test_reg(self):
        list = [3, 4, 5, 10, 8]
        result = hw4p2.ListAvg(list)
        self.assertEqual(result, 6)

    def test_none(self):
        list = []
        result = hw4p2.ListAvg(list)
        self.assertEqual(result, 0)

    def test_letters(self):
        list = ["1", "3"]
        result = hw4p2.ListAvg(list)
        self.assertEqual(result, 0)

    if __name__ == "__main__":
        unittest.main()
