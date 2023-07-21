# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, balanced = self.isNodeBalanced(root, True)
        return balanced

    def isNodeBalanced(self, node: TreeNode, balanced: bool):
        if not node:
            return 0, balanced
        left_edge, left_balance = self.isNodeBalanced(node.left, balanced)
        right_edge, right_balance = self.isNodeBalanced(node.right, balanced)

        if left_edge - right_edge < -1 or left_edge - right_edge > 1:
            balanced = False
        return (
            max(left_edge, right_edge) + 1,
            balanced and left_balance and right_balance,
        )
