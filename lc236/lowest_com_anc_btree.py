# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = root
        def dfs(node) -> bool:
            nonlocal answer
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)
            mid = node.val == p.val or node.val == q.val

            if left + right + mid >= 2:
                answer = node

            return mid or left or right

        dfs(root)
        return answer