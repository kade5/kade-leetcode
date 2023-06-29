class MinStack(object):
    def __init__(self):
        self.stack = []
        self.length = 0
        self.minimum_value = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.length += 1
        if self.length == 1:
            self.minimum_value.append(val)
        elif len(self.minimum_value) == 0 or val <= self.minimum_value[-1]:
            self.minimum_value.append(val)

    def pop(self):
        """
        :rtype: None
        """
        element = self.stack.pop()
        self.length -= 1
        if element == self.minimum_value[-1]:
            self.minimum_value.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.length == 0:
            return None
        return self.stack[self.length - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minimum_value) == 0:
            return None
        return self.minimum_value[-1]
