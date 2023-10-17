from collections import deque


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        visited = set()
        queue = deque()
        queue.append(0)

        while queue:
            cur = queue.popleft()
            if cur in visited:
                return False

            visited.add(cur)

            if leftChild[cur] != -1:
                queue.append(leftChild[cur])

            if rightChild[cur] != -1:
                queue.append(rightChild[cur])

        return len(visited) == n
