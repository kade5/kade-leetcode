import unittest
from min_stack import MinStack


class TestSolution(unittest.TestCase):
    def test_normal(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        value1 = minStack.getMin()  # return -3
        self.assertEqual(value1, -3)
        minStack.pop()
        value2 = minStack.top()  # return 0
        self.assertEqual(value2, 0)
        value3 = minStack.getMin()  # return -2
        self.assertEqual(value3, -2)

    def test_normal2(self):
        minStack = MinStack()
        minStack.push(85)
        minStack.push(-99)
        minStack.push(67)
        value1= minStack.getMin()
        self.assertEqual(value1, -99)


if __name__ == "__main__":
    unittest.main()
