import unittest
from binary_search import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [-1, 0, 3, 5, 9, 12]
        target = 9
        correct_output = 4
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_negative(self):
        input = [-1, 0, 3, 5, 9, 12]
        target = 2
        correct_output = -1
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_one(self):
        input = [5]
        target = 5
        correct_output = 0
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_two(self):
        input = [2, 5]
        target = 5
        correct_output = 1
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_two_negative(self):
        input = [2, 5]
        target = 0
        correct_output = -1
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
