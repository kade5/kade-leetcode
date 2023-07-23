package lc102

// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	var nodeSlice [][]int
	addNode(root, &nodeSlice, 0)
	return nodeSlice
    
}

func addNode(node *TreeNode, nodeSlice *[][]int, level int) {
	if node == nil {
		return
	}
	if len(*nodeSlice) < level + 1 {
		var newLevel []int
		*nodeSlice = append(*nodeSlice, newLevel)
	}
	(*nodeSlice)[level] = append((*nodeSlice)[level], node.Val)
	addNode(node.Left, nodeSlice, level + 1)
	addNode(node.Right, nodeSlice, level + 1)
}
