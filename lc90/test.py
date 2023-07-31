import unittest
from subsets_II import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal_example(self):
        input = [1,2,2]
        correct_output = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        test_output = self.solution.subsetsWithDup(input)
        self.assertCountEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
