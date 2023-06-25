import unittest
from group_anagrams import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_with_3_letter_words(self):
        test1_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        test1_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual1_output = self.solution.groupAnagramsRework(test1_input)
        self.assertCountEqual(actual1_output, test1_output)

    def test_with_empty_string(self):
        test_input = [""]
        test_output = [[""]]
        self.assertCountEqual(self.solution.groupAnagramsRework(test_input), test_output)


if __name__ == "__main__":
    unittest.main()
