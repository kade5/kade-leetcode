import unittest
from search_rotated_array import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        correct_output = 4
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_negative(self):
        input = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        correct_output = -1
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_one(self):
        input = [1]
        target = 0
        correct_output = -1
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_normal2(self):
        input = [3, 5, 1]
        target = 3
        correct_output = 0
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)

    def test_two_elements(self):
        input = [1, 3]
        target = 3
        correct_output = 1
        test_output = self.solution.search(input, target)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
