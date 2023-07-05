import unittest
from time_map import TimeMap


class TestSolution(unittest.TestCase):

    def test_normal(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 2)
        self.assertEqual(time_map.get("foo", 2), "bar")
        self.assertEqual(time_map.get("foo", 3), "bar")
        time_map.set("foo", "bar2", 4)
        self.assertEqual(time_map.get("foo", 4), "bar2")
        self.assertEqual(time_map.get("foo", 5), "bar2")
        self.assertEqual(time_map.get("foo", 1), "")


if __name__ == "__main__":
    unittest.main()
