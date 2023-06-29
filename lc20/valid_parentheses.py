class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters
        '(', ')', '{', '}', '[' and ']', determine if the input string
        is valid.

        An input string is valid if:

            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same
            type.
                :type s: str
                :rtype: bool
        """
        stack = []
        corresponding_brace = {"(": ")", "[": "]", "{": "}"}

        for character in s:
            if corresponding_brace.get(character):
                stack.append(character)
            else:
                if len(stack) == 0 or corresponding_brace.get(stack.pop()) != character:
                    return False

        if len(stack) > 0:
            return False

        return True
