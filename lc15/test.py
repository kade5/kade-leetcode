import unittest
from three_sum import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [-1, 0, 1, 2, -1, -4]
        correct_output = [[-1, -1, 2], [-1, 0, 1]]
        test_output = self.solution.threeSum(input)
        self.assertCountEqual(test_output, correct_output)

    def test_negative(self):
        input = [0, 1, 1]
        correct_output = []
        test_output = self.solution.threeSum(input)
        self.assertCountEqual(test_output, correct_output)

    def test_zeros(self):
        input = [0, 0, 0]
        correct_output = [[0, 0, 0]]
        test_output = self.solution.threeSum(input)
        self.assertCountEqual(test_output, correct_output)

    def test_four_zeros(self):
        input = [0, 0, 0, 0]
        correct_output = [[0, 0, 0]]
        test_output = self.solution.threeSum(input)
        self.assertCountEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
