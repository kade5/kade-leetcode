import unittest
from minimum_element import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [3, 4, 5, 1, 2]
        correct_output = 1
        test_output = self.solution.findMin(input)
        self.assertEqual(test_output, correct_output)

    def test_normal2(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        correct_output = 0
        test_output = self.solution.findMin(input)
        self.assertEqual(test_output, correct_output)

    def test_normal3(self):
        input = [11, 13, 15, 17]
        correct_output = 11
        test_output = self.solution.findMin(input)
        self.assertEqual(test_output, correct_output)

    def test_one_element(self):
        input = [3]
        correct_output = 3
        test_output = self.solution.findMin(input)
        self.assertEqual(test_output, correct_output)

    def test_normal4(self):
        input = [4, 5, 1, 2, 3]
        correct_output = 1
        test_output = self.solution.findMin(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
