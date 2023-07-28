# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = []
        encoded = ""
        if root:
            queue.append(root)
            encoded += str(root.val)

        while queue:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
                encoded = encoded + "," + str(current_node.left.val)
            else:
                encoded += ",n"
            if current_node.right:
                queue.append(current_node.right)
                encoded = encoded + "," + str(current_node.right.val)
            else:
                encoded += ",n"

        return encoded

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        head = None
        queue = []

        if data:
            head = TreeNode(data_list.pop(0))
            queue.append(head)

        while queue:
            current_node = queue.pop(0)
            left = data_list.pop(0)
            right = data_list.pop(0)

            if left != "n":
                left_node = TreeNode(int(left))
                current_node.left = left_node
                queue.append(left_node)

            if right != "n":
                right_node = TreeNode(int(right))
                current_node.right = right_node
                queue.append(right_node)

        return head

