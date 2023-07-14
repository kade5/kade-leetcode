# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        next_node = head
        node_hash = {}

        while next_node:
            new_node = Node(next_node.val)
            node_hash[next_node] = new_node
            next_node = next_node.next

        next_node = head

        while next_node:
            new_node = node_hash[next_node]
            new_node.next = node_hash.get(next_node.next, None)
            new_node.random = node_hash.get(next_node.random, None)
            next_node = next_node.next

        return node_hash.get(head, None)
