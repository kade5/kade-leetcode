import unittest
from find_duplicate import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input_1 = [1, 3, 4, 2, 2]
        correct_output = 2
        test_output = self.solution.findDuplicate(input_1)
        self.assertEqual(test_output, correct_output)

    def test_normal_2(self):
        input_1 = [3, 1, 3, 4, 2]
        correct_output = 3
        test_output = self.solution.findDuplicate(input_1)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
