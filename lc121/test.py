import unittest
from stock import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [7, 1, 5, 3, 6, 4]
        correct_output = 5
        test_output = self.solution.maxProfit(input)
        self.assertEqual(test_output, correct_output)

    def test_no_profit(self):
        input = [7, 6, 4, 3, 1]
        correct_output = 0
        test_output = self.solution.maxProfit(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
