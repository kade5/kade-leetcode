import unittest
from matrix_search import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        correct_output = True
        test_output = self.solution.searchMatrix(input, target)
        self.assertEqual(test_output, correct_output)

    def test_negative(self):
        input = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        correct_output = False
        test_output = self.solution.searchMatrix(input, target)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
