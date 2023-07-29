import unittest
from subsets import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal_example(self):
        input = [1,2,3]
        correct_output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        test_output = self.solution.subsets(input)
        self.assertCountEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
