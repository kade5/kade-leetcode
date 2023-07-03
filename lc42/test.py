import unittest
from trapping_rainwater import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        correct_output = 6
        test_output = self.solution.trap(input)
        self.assertEqual(test_output, correct_output)

    def test_normal2(self):
        input = [4, 2, 0, 3, 2, 5]
        correct_output = 9
        test_output = self.solution.trap(input)
        self.assertEqual(test_output, correct_output)

    def test_normal3(self):
        input = [4, 3, 6, 1, 2, 1, 2, 2, 1, 1]
        correct_output = 3
        test_output = self.solution.trap(input)
        self.assertEqual(test_output, correct_output)

    def test_end_zeroes(self):
        input = [0, 2, 0]
        correct_output = 0
        test_output = self.solution.trap(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
