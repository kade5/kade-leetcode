import unittest
from most_water import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        correct_output = 49
        test_output = self.solution.maxArea(input)
        self.assertEqual(test_output, correct_output)

    def test_two_elements(self):
        input = [1, 1]
        correct_output = 1
        test_output = self.solution.maxArea(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
