
// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	return nodeHasSubTree(root, subRoot, subRoot)

}

func nodeHasSubTree(node *TreeNode, subNode *TreeNode, subRoot *TreeNode) bool {
	if subNode == nil && node == nil {
		return true
	}
	if node == nil {
		return false
	}
	if node != nil && subNode != nil && node.Val == subNode.Val {
		return nodeHasSubTree(node.Left, subNode.Left, subRoot) && nodeHasSubTree(node.Right, subNode.Right, subRoot)
	}
	return nodeHasSubTree(node.Left, subRoot, subRoot) || nodeHasSubTree(node.Right, subRoot, subRoot)
}
