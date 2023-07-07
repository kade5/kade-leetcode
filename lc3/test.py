import unittest
from unique_characters import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = "abcabcbb"
        correct_output = 3
        test_output = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(test_output, correct_output)

    def test_same_letter(self):
        input = "bbbbb"
        correct_output = 1
        test_output = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(test_output, correct_output)

    def test_normal2(self):
        input = "pwwkew"
        correct_output = 3
        test_output = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
