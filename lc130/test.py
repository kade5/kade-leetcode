import unittest
from surrounded_regions import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal_example(self):
        input = [
            ["O", "X", "X", "O", "X"],
            ["X", "O", "O", "X", "O"],
            ["X", "O", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"],
        ]
        correct_output = [
            ["O", "X", "X", "O", "X"],
            ["X", "X", "X", "X", "O"],
            ["X", "X", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"],
        ]
        self.solution.solve(input)
        self.assertCountEqual(input, correct_output)

if __name__ == "__main__":
    unittest.main()
