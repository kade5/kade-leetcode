# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_edge = self.maxEdge(root.left, 0)
        right_edge = self.maxEdge(root.right, 0)

        if -1 <= left_edge - right_edge <= 1:
            return True
        return False

    def maxEdge(self, node: TreeNode, max_edge: int) -> int:
        if not node:
            return max_edge
        return max(
            self.maxEdge(node.left, max_edge + 1),
            self.maxEdge(node.right, max_edge + 1),
        )
