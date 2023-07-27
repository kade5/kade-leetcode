# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_value = -1001

        def maxNodeSum(node: TreeNode):
            nonlocal max_value
            if node is None:
                return 0, 0

            ll, lr = maxNodeSum(node.left)
            rl, rr = maxNodeSum(node.right)
            largest_left = max(ll, lr)
            largest_right = max(rl, rr)
            max_value = max(
                greatestSum(largest_left, largest_right, node.val), max_value
            )
            return max(largest_left + node.val, node.val), max(
                largest_right + node.val, node.val
            )

        def greatestSum(left, right, value):
            return max(value, value + left, value + right, value + left + right)

        _, _ = maxNodeSum(root)
        return max_value
