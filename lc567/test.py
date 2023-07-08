import unittest
from permutation import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_true(self):
        test_input = "ab"
        s2_input = "eidbaooo"
        test_output = True
        actual_output = self.solution.checkInclusion(
            test_input, s2_input
        )
        self.assertEqual(actual_output, test_output)

    def test_false(self):
        test_input = "ab"
        s2_input = "eidboaoo"
        test_output = False
        actual_output = self.solution.checkInclusion(
            test_input, s2_input
        )
        self.assertEqual(actual_output, test_output)

    def test_3_true(self):
        test_input = "adc"
        s2_input = "dcda"
        test_output = True
        actual_output = self.solution.checkInclusion(
            test_input, s2_input
        )
        self.assertEqual(actual_output, test_output)


if __name__ == "__main__":
    unittest.main()
