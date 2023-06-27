import unittest
from valid_palindrome import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = "A man, a plan, a canal: Panama"
        correct_output = True
        test_output = self.solution.isPalindrome(input)
        self.assertEqual(test_output, correct_output)

    def test_negative(self):
        input = "race a car"
        correct_output = False
        test_output = self.solution.isPalindrome(input)
        self.assertEqual(test_output, correct_output)

    def test_blank_space(self):
        input = " "
        correct_output = True
        test_output = self.solution.isPalindrome(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
