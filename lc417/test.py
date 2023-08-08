import unittest
from water_flow import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal_example(self):
        input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        correct_output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        test_output = self.solution.pacificAtlantic(input)
        self.assertCountEqual(test_output, correct_output)

    def test_normal_example2(self):
        input = [[1,1],[1,1],[1,1]]
        correct_output = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
        test_output = self.solution.pacificAtlantic(input)
        self.assertCountEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
