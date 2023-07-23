# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, root.val)

    def traverse(self, node: TreeNode, max_value: float) -> int:
        count_value = 0
        if not node:
            return count_value
        if node.val >= max_value:
            max_value = node.val
            count_value += 1
        return (
            self.traverse(node.left, max_value)
            + self.traverse(node.right, max_value)
            + count_value
        )
