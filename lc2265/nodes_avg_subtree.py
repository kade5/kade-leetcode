# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: TreeNode):
            nonlocal result
            sum = node.val
            count = 1

            if node.left:
                lsum, lcount = dfs(node.left)
                sum += lsum
                count += lcount

            if node.right:
                lsum, lcount = dfs(node.right)
                sum += lsum
                count += lcount

            if sum // count == node.val:
                result += 1

            return sum, count

        dfs(root)
        return result
