# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        current_head = head
        current_tail = None
        next_head = None
        dummy_head = ListNode(0, head)
        previous_tail = dummy_head

        while True:
            current_tail = self.traverseK(current_head, k)
            if not current_tail:
                break
            next_head = current_tail.next
            current_tail.next = None
            previous_tail.next = None
            current_tail = current_head
            current_head = self.reverseList(current_head)
            current_tail.next = next_head
            previous_tail.next = current_head
            previous_tail = current_tail
            current_head = next_head


        return dummy_head.next



    def traverseK(self, head: ListNode, k: int) -> ListNode:
        current_node = head
        while k > 1 and current_node:
            current_node = current_node.next
            if not current_node:
                break
            k -= 1
        return current_node

    def reverseList(self, head: ListNode) -> ListNode:
        """
        Given the head of a singly linked list, reverse the list, and return
        the reversed list.
        """
        current_node = head
        next_node = None
        previous_node = None
        while current_node and current_node.next:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        if current_node:
            current_node.next = previous_node

        return current_node
