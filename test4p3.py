import unittest
import hw4p3

class NameTest(unittest.TestCase):
    def test_reg(self):
        result = hw4p3.NameGen("John", "Doe")
        self.assertEqual(result, "John Doe")

    def test_num(self):
        result = hw4p3.NameGen("John", 5)
        self.assertEqual(result, "Error!")

    def test_xtraSpace(self):
        result = hw4p3.NameGen("John ", "Doe")
        self.assertEqual(result, "John  Doe")

    if __name__ == "__main__":
        unittest.main()
