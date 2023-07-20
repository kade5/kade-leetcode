# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = 0
        _, max_diameter = self.diameterOfNode(root, max_diameter)
        return max_diameter

    def diameterOfNode(self, node: TreeNode, max_diameter: int):
        left_edge = right_edge = max_left_diameter = max_right_diameter = 0

        if node.left:
            left_edge, max_left_diameter = self.diameterOfNode(node.left, max_diameter)
        if node.right:
            right_edge, max_right_diameter = self.diameterOfNode(
                node.right, max_diameter
            )

        return max(left_edge, right_edge) + 1, max(
            max_left_diameter, max_right_diameter, max_diameter, left_edge + right_edge
        )
