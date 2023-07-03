import unittest
from largest_rect import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [2, 1, 5, 6, 2, 3]
        correct_output = 10
        test_output = self.solution.largestRectangleArea(input)
        self.assertEqual(test_output, correct_output)

    def test_two(self):
        input = [2, 4]
        correct_output = 4
        test_output = self.solution.largestRectangleArea(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
