import unittest
from daily_temps import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_example(self):
        input = [73, 74, 75, 71, 69, 72, 76, 73]
        correct_output = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(self.solution.dailyTemperatures(input), correct_output)

    def test_increasing(self):
        input = [30, 40, 50, 60]
        correct_output = [1, 1, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(input), correct_output)

    def test_three(self):
        input = [30, 60, 90]
        correct_output = [1, 1, 0]
        self.assertEqual(self.solution.dailyTemperatures(input), correct_output)

if __name__ == "__main__":
    unittest.main()
