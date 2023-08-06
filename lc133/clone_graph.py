from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node):
        visited = {}
        queue = deque()
        head = None
        if node:
            head = Node(node.val)
            visited[node] = head
            queue.append(node)

        while queue:
            parent = queue.popleft()

            for adj in parent.neighbors:
                if adj not in visited:
                    visited[adj] = Node(adj.val)
                    queue.append(adj)
                visited[parent].neighbors.append(visited[adj])


        return head
