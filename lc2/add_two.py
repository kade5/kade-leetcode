# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node = l1
        l2_node = l2
        previous_node = None
        l1_values = []
        l2_values = []
        combined_nodes = []

        while l1_node or l2_node:
            if l1_node:
                l1_values.append(l1_node.val)
                l1_node = l1_node.next
            if l2_node:
                l2_values.append(l2_node.val)
                l2_node = l2_node.next
            new_node = ListNode()
            if previous_node:
                previous_node.next = new_node
            previous_node = new_node
            combined_nodes.append(new_node)

        extra = 0
        values = 0

        for i in range(1, max(len(l1_values), len(l2_values)) + 1):
            values = extra
            if i <= len(l1_values):
                values += l1_values[-i]
            if i <= len(l2_values):
                values += l2_values[-i]
            extra = values // 10
            combined_nodes[-i].val = values % 10

        if values < 10:
            return combined_nodes[0]

        combined_head = ListNode(values // 10, combined_nodes[0])
        combined_nodes[0].val = values % 10
        return combined_head
