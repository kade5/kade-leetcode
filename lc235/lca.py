# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        node_set = set()
        current_node = root
        result = root
        node_set.add(current_node)

        while current_node.val != p.val:
            if p.val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
            node_set.add(current_node)

        current_node = root

        while current_node.val != q.val:
            if q.val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node in node_set:
                result = current_node

        return result
