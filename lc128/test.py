import unittest
from longest_sequence import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [100, 4, 200, 1, 3, 2]
        correct_output = 4
        test_output = self.solution.longestConsecutive(input)
        self.assertEqual(test_output, correct_output)

    def test_duplicate_values(self):
        input = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        correct_output = 9
        test_output = self.solution.longestConsecutive(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
