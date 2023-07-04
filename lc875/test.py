import unittest
from eating_bananas import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = [3, 6, 7, 11]
        hours = 8
        correct_output = 4
        test_output = self.solution.minEatingSpeed(input, hours)
        self.assertEqual(test_output, correct_output)

    def test_normal2(self):
        input = [30, 11, 23, 4, 20]
        hours = 5
        correct_output = 30
        test_output = self.solution.minEatingSpeed(input, hours)
        self.assertEqual(test_output, correct_output)

    def test_normal3(self):
        input = [30, 11, 23, 4, 20]
        hours = 6
        correct_output = 23
        test_output = self.solution.minEatingSpeed(input, hours)
        self.assertEqual(test_output, correct_output)

    def test_normal4(self):
        input = [
            332484035,
            524908576,
            855865114,
            632922376,
            222257295,
            690155293,
            112677673,
            679580077,
            337406589,
            290818316,
            877337160,
            901728858,
            679284947,
            688210097,
            692137887,
            718203285,
            629455728,
            941802184,
        ]
        hours = 823855818
        correct_output = 14
        test_output = self.solution.minEatingSpeed(input, hours)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
