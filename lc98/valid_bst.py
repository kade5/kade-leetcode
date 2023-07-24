# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left_val = root.left.val if root.left else None
        right_val = root.right.val if root.right else None

        if (left_val and root.val <= left_val) or (right_val and root.val >= right_val):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)

