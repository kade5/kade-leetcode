class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        stack = []
        hash_map = {}

        for i, c in enumerate(s):
            if c in hash_map:
                while stack and stack[-1] > hash_map[c]:
                    stack.pop()
            else:
                hash_map[c] = i
                stack.append(i)

        prev = 0
        result = []
        for i in stack:
            if i == 0:
                continue
            result.append(i - prev)
            prev = i

        result.append(len(s) - prev)
        return result
