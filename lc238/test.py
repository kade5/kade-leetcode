import unittest
from product_array import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [1, 2, 3, 4]
        correct_output = [24, 12, 8, 6]
        test_output = self.solution.productExceptSelf(input)
        self.assertEqual(test_output, correct_output)

    def test_with_zeros(self):
        input = [-1, 1, 0, -3, 3]
        correct_output = [0, 0, 9, 0, 0]
        test_output = self.solution.productExceptSelf(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
