# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        dummy = TreeNode(0, root, None)
        max_depth = self.getDepth(dummy, 0)
        
        return max_depth
    def getDepth(self, root: TreeNode, depth: int) -> int:
        depth_left = depth_right = depth

        if root.right:
            depth_right = self.getDepth(root.right, depth + 1)
        if root.left:
            depth_left = self.getDepth(root.left, depth + 1)

        return max(depth_left, depth_right)

