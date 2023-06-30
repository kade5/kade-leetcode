class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Given n pairs of parentheses, write a function to generate all
        combinations of well-formed parentheses.
                :type n: int
                :rtype: List[str]
        """
        left = n
        right = n
        result = []
        stack = ""
        current_set = ""

        self.workFunction(left, right, stack, current_set, result)
        return result

    def workFunction(self, left, right, stack, current_set, result):
        if left == 0 and right == 0:
            result.append(current_set)
            return
        if len(stack) > 0:
            self.workFunction(left, right - 1, stack[:-1], current_set + ")", result)
        if left > 0:
            self.workFunction(left - 1, right, stack + ")", current_set + "(", result)
