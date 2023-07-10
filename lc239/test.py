import unittest
from slide_window_max import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input_1 = [1, 3, -1, -3, 5, 3, 6, 7]
        input_2 = 3
        correct_output = [3, 3, 5, 5, 6, 7]
        test_output = self.solution.maxSlidingWindow(input_1, input_2)
        self.assertEqual(test_output, correct_output)

    def test_one(self):
        input_1 = [1]
        input_2 = 1
        correct_output = [1]
        test_output = self.solution.maxSlidingWindow(input_1, input_2)
        self.assertEqual(test_output, correct_output)

    def test_three(self):
        input_1 = [7, 2, 4]
        input_2 = 2
        correct_output = [7, 4]
        test_output = self.solution.maxSlidingWindow(input_1, input_2)
        self.assertEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
