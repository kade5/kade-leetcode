# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        node = root
        while node.left:
            node = node.left
            self.stack.append(node)

        self.pointer = node.val - 1


    def next(self) -> int:
        node = self.stack.pop()
        self.pointer = node.val

        if node.right:
            self.stack.append(node.right)
            node = node.right
            while node.left:
                node = node.left
                self.stack.append(node)

        return self.pointer


    def hasNext(self) -> bool:
        return len(self.stack) > 0