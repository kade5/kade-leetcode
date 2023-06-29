import unittest
from reverse_polish import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = ["2", "1", "+", "3", "*"]
        correct_output = 9
        self.assertEqual(self.solution.evalRPN(input), correct_output)

    def test_division(self):
        input = ["4", "13", "5", "/", "+"]
        correct_output = 6
        self.assertEqual(self.solution.evalRPN(input), correct_output)

    def test_long(self):
        input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        correct_output = 22
        self.assertEqual(self.solution.evalRPN(input), correct_output)


if __name__ == "__main__":
    unittest.main()
