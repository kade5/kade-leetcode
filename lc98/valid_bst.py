import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, -math.inf, math.inf)

    def isValid(self, node, left_bound, right_bound) -> bool:
        if not node:
            return True
        if node.val <= left_bound or node.val >= right_bound:
            return False
        return self.isValid(node.left, left_bound, node.val) and self.isValid(
            node.right, node.val, right_bound
        )
