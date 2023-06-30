import unittest
from generate_parentheses import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_n_1(self):
        input = 1
        correct_output = ["()"]
        self.assertCountEqual(self.solution.generateParenthesis(input), correct_output)

    def test_n_2(self):
        input = 2
        correct_output = ["(())", "()()"]
        self.assertCountEqual(self.solution.generateParenthesis(input), correct_output)

    def test_n_3(self):
        input = 3
        correct_output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(self.solution.generateParenthesis(input), correct_output)


if __name__ == "__main__":
    unittest.main()
