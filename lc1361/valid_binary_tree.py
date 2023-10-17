from collections import deque


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        head = self.findHead(n, leftChild, rightChild)
        if head == -1:
            return False
        queue = deque()
        queue.append(head)
        visited = set()

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

    def findHead(self, n: int, leftChild: list[int], rightChild: list[int]) -> int:
        visited = set(range(n))

        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] not in visited:
                    return -1
                visited.remove(leftChild[i])
            if rightChild[i] != -1:
                if rightChild[i] not in visited:
                    return -1
                visited.remove(rightChild[i])

        if len(visited) != 1:
            return -1
        return list(visited)[0]
