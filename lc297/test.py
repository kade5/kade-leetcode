import unittest
from encode_tree import Codec


class TestSolution(unittest.TestCase):
    solution = Codec()

    def test_normal(self):
        input = ""
        correct_output = None
        test_output = self.solution.deserialize(input)
        self.assertEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
