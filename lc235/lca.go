package lc235

// Definition for a binary tree node.
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	currentNode := root

	for {
		if currentNode.Val < p.Val && currentNode.Val < q.Val {
			currentNode = currentNode.Right
		} else if currentNode.Val > p.Val && currentNode.Val > q.Val {
			currentNode = currentNode.Left
		} else {
			break	
		}
	}
	return currentNode
}
