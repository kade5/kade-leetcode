import unittest
from encode_strings import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_encode1(self):
        input = ["lint", "code", "love", "you"]
        correct_output = "4|lint4|code4|love3|you"
        test_output = self.solution.encode(input)
        self.assertEqual(test_output, correct_output)

    def test_decode1(self):
        input = "4|lint4|code4|love3|you"
        correct_output = ["lint", "code", "love", "you"]
        test_output = self.solution.decode(input)
        self.assertEqual(test_output, correct_output)

    def test_encode_with_bar(self):
        input = ["we", "say", "|", "yes"]
        correct_output = "2|we3|say1||3|yes"
        test_output = self.solution.encode(input)
        self.assertEqual(test_output, correct_output)

    def test_decode_with_bar(self):
        input = "2|we3|say1||3|yes"
        correct_output = ["we", "say", "|", "yes"]
        test_output = self.solution.decode(input)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
