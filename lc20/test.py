import unittest
from valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_one_set(self):
        input = "()"
        correct_output = True
        test_output = self.solution.isValid(input)
        self.assertEqual(test_output, correct_output)

    def test_consecutive(self):
        input = "()[]{}"
        correct_output = True
        test_output = self.solution.isValid(input)
        self.assertEqual(test_output, correct_output)

    def test_mismatch(self):
        input = "(]"
        correct_output = False
        test_output = self.solution.isValid(input)
        self.assertEqual(test_output, correct_output)

    def test_no_closing(self):
        input = "([{"
        correct_output = False
        test_output = self.solution.isValid(input)
        self.assertEqual(test_output, correct_output)

    def test_closing_only(self):
        input = "}"
        correct_output = False
        test_output = self.solution.isValid(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
