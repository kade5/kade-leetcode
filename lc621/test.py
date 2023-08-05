import unittest
from task_scheduler import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input = ["A","A","A","B","B","B"]
        target = 2
        correct_output = 8
        test_output = self.solution.leastInterval(input, target)
        self.assertEqual(test_output, correct_output)

    def test_0_cool(self):
        input = ["A","A","A","B","B","B"]
        target = 0
        correct_output = 6
        test_output = self.solution.leastInterval(input, target)
        self.assertEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
