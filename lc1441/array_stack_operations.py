class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack = []
        result = []
        index = 0
        pop_count = 0
        n = 1

        def apply_push(n):
            stack.append(n)
            result.append("Push")

        def apply_pop(c):
            while c > 0:
                stack.pop()
                result.append("Pop")
                c -= 1

        while index < len(target):
            if n < target[index]:
                apply_push(n)
                pop_count += 1
                n += 1

            elif target[index] == n:
                apply_pop(pop_count)
                pop_count = 0
                apply_push(n)
                n += 1
                index += 1

        return result
