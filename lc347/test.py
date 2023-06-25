import unittest
from top_k_freq_elem import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def normal_example(self):
        input = [1,1,1,2,2,3]
        correct_output = [1,2]
        self.assertCountEqual(self.solution.topKFrequent(input, 2), correct_output)

    def one_number_example(self):
        input = [1]
        correct_output = [1]
        self.assertCountEqual(self.solution.topKFrequent(input, 1), correct_output)

if __name__ == "__main__":
    unittest.main()
