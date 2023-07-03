import unittest
from car_fleet import Solution


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal(self):
        input_pos = [10, 8, 0, 5, 3]
        input_speed = [2, 4, 1, 1, 3]
        input_target = 12
        correct_output = 3
        test_output = self.solution.carFleet(input_target, input_pos, input_speed)
        self.assertEqual(test_output, correct_output)

    def test_one_car(self):
        input_pos = [3]
        input_speed = [3]
        input_target = 10
        correct_output = 1
        test_output = self.solution.carFleet(input_target, input_pos, input_speed)
        self.assertEqual(test_output, correct_output)

    def test_one_fleet(self):
        input_pos = [0, 2, 4]
        input_speed = [4, 2, 1]
        input_target = 100
        correct_output = 1
        test_output = self.solution.carFleet(input_target, input_pos, input_speed)
        self.assertEqual(test_output, correct_output)

    def test_two_cars(self):
        input_pos = [6, 8]
        input_speed = [3, 2]
        input_target = 10
        correct_output = 2
        test_output = self.solution.carFleet(input_target, input_pos, input_speed)
        self.assertEqual(test_output, correct_output)

    def test_6_fleet(self):
        input_pos = [8, 3, 7, 4, 6, 5]
        input_speed = [4, 4, 4, 4, 4, 4]
        input_target = 10
        correct_output = 6
        test_output = self.solution.carFleet(input_target, input_pos, input_speed)
        self.assertEqual(test_output, correct_output)


if __name__ == "__main__":
    unittest.main()
