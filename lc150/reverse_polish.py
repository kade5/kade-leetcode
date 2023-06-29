class Solution(object):
    def evalRPN(self, tokens: list[str]) -> int:
        """
        You are given an array of strings tokens that represents an
        arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the
        value of the expression.
                :type tokens: List[str]
                :rtype: int
        """
        stack = []
        expressions = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in expressions:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calculate(num1, num2, token))

        return stack.pop()

    def calculate(self, num1: int, num2: int, expression: str) -> int:
        match expression:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(num1 / num2)
            case _:
                return 0
