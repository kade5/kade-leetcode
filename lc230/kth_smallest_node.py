# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        dummy = TreeNode(0, root, None)
        currentNode = root
        stack = []
        counter = 0
        stack.append(dummy)

        while stack:
            while currentNode.left:
                stack.append(currentNode)
                tmp = currentNode.left
                currentNode.left = None
                currentNode = tmp
            counter += 1
            if counter == k:
                return currentNode.val
            if currentNode.right:
                currentNode = currentNode.right
            else:
                currentNode = stack.pop()
        return root.val
