# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node_set = set()
        next_node = head

        while next_node:
            if next_node in node_set:
                return True
            node_set.add(next_node)
            next_node = next_node.next


        return False
