class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        def logic(c, stack):
            if c == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)

        for c in s:
            logic(c, stack_s)
        for c in t:
            logic(c, stack_t)

        return stack_s == stack_t

