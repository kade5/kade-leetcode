import unittest
from repeat_char_replacement import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_4_letters(self):
        test_input = "ABAB"
        replacement_input = 2
        test_output = 4
        actual_output = self.solution.characterReplacement(
            test_input, replacement_input
        )
        self.assertEqual(actual_output, test_output)

    def test_7_letters(self):
        test_input = "AABABBA"
        replacement_input = 1
        test_output = 4
        actual_output = self.solution.characterReplacement(
            test_input, replacement_input
        )
        self.assertEqual(actual_output, test_output)


if __name__ == "__main__":
    unittest.main()
