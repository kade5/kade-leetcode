from list_node import ListNode
class Solution:
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

