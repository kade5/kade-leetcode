import unittest
from two_sum import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal_example(self):
        input = [2, 7, 11, 15]
        correct_output = [0, 1]
        test_output = self.solution.twoSum(input, 9)
        self.assertCountEqual(test_output, correct_output)

    def test_normal_example2(self):
        input = [3, 2, 4]
        correct_output = [1, 2]
        test_output = self.solution.twoSum(input, 6)
        self.assertCountEqual(test_output, correct_output)

    def test_duplicate_num_example(self):
        input = [3, 3]
        correct_output = [0, 1]
        test_output = self.solution.twoSum(input, 6)
        self.assertCountEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
