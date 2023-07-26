# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        int_array = []
        self.traverse(root, int_array)
        return int_array

    def traverse(self, node, int_array):
        if node is None:
            return
        self.traverse(node.left, int_array)
        int_array.append(node.val)
        self.traverse(node.right, int_array)
