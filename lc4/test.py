import unittest
from median_two_ararys import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input_1 = [1, 3]
        input_2 = [2]
        correct_output = 2.0
        test_output = self.solution.findMedianSortedArrays(input_1, input_2)
        self.assertEqual(test_output, correct_output)

    def test_even(self):
        input_1 = [1, 2]
        input_2 = [3, 4]
        correct_output = 2.5
        test_output = self.solution.findMedianSortedArrays(input_1, input_2)
        self.assertEqual(test_output, correct_output)

    def test_10(self):
        input_1 = [1, 2, 5, 7, 8, 10]
        input_2 = [3, 4, 6, 9]
        correct_output = 5.5
        test_output = self.solution.findMedianSortedArrays(input_1, input_2)
        self.assertEqual(test_output, correct_output)

    def test_empty2(self):
        input_1 = [2]
        input_2 = []
        correct_output = 2
        test_output = self.solution.findMedianSortedArrays(input_1, input_2)
        self.assertEqual(test_output, correct_output)

    def test_empty2_2one(self):
        input_1 = [3, 4]
        input_2 = []
        correct_output = 3.5
        test_output = self.solution.findMedianSortedArrays(input_1, input_2)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
