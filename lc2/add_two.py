# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node = l1
        l2_node = l2
        extra = 0
        value = 0
        head = None
        previous_node = None

        while l1_node or l2_node:
            value = extra
            if l1_node:
                value += l1_node.val
                l1_node = l1_node.next
            if l2_node:
                value += l2_node.val
                l2_node = l2_node.next
            new_node = ListNode(value % 10)
            if previous_node:
                previous_node.next = new_node
            if not head:
                head = new_node
            extra = value // 10
            previous_node = new_node

        if extra > 0:
            new_node = ListNode(extra)
            previous_node.next = new_node


        return head
