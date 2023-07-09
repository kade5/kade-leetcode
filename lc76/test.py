import unittest
from min_window_substring import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = "ADOBECODEBANC"
        input_t = "ABC"
        correct_output = "BANC"
        test_output = self.solution.minWindow(input, input_t)
        self.assertEqual(test_output, correct_output)

    def test_single(self):
        input = "a"
        input_t = "a"
        correct_output = "a"
        test_output = self.solution.minWindow(input, input_t)
        self.assertEqual(test_output, correct_output)

    def test_negative(self):
        input = "a"
        input_t = "aa"
        correct_output = ""
        test_output = self.solution.minWindow(input, input_t)
        self.assertEqual(test_output, correct_output)

    def test_last(self):
        input = "bbbbbbba"
        input_t = "a"
        correct_output = "a"
        test_output = self.solution.minWindow(input, input_t)
        self.assertEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
