import unittest
from reverse_linked_list import Solution
from list_node import ListNode


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_normal_example(self):
        node5 = ListNode(5, None)
        node4 = ListNode(4, node5)
        node3 = ListNode(3, node4)
        node2 = ListNode(2, node3)
        head = ListNode(1, node2)
        input = head
        correct_output = head
        test_output = self.solution.reverseList(head)
        self.assertCountEqual(test_output, correct_output)

if __name__ == "__main__":
    unittest.main()
