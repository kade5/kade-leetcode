import unittest
from two_sum_ii import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [2, 7, 11, 15]
        correct_output = [1, 2]
        test_output = self.solution.twoSum(input, 9)
        self.assertEqual(test_output, correct_output)

    def test_normal2(self):
        input = [2, 3, 4]
        correct_output = [1, 3]
        test_output = self.solution.twoSum(input, 6)
        self.assertEqual(test_output, correct_output)

    def test_negative(self):
        input = [-1, 0]
        correct_output = [1, 2]
        test_output = self.solution.twoSum(input, -1)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
