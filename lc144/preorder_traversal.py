# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        int_list = []
        self.traverse(root, int_list)
        return int_list

    def traverse(self, node: TreeNode, int_list: list[int]):
        if node is None:
            return
        int_list.append(node.val)
        self.traverse(node.left, int_list)
        self.traverse(node.right, int_list)
