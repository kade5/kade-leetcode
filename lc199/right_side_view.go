package lc199

// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	var result []int
	var queue []*TreeNode
	var levelQueue []int
	if root != nil {
		queue = append(queue, root)
		levelQueue = append(levelQueue, 0)
	}
	
	for len(queue) > 0 {
		var node *TreeNode
		var index int
		node, queue = dequeue(queue)
		index, levelQueue = dequeueLevel(levelQueue)

		if node != nil {
			result = addResult(result, node.Val, index)
			queue = append(queue, node.Left)
			levelQueue = append(levelQueue, index + 1)
			queue = append(queue, node.Right)
			levelQueue = append(levelQueue, index + 1)
		}
	}

	return result
}

func dequeue(queue []*TreeNode) (*TreeNode, []*TreeNode) {
	return queue[0], queue[1:]	
}

func dequeueLevel(queue []int) (int, []int) {
	return queue[0], queue[1:]
}

func addResult(result []int, value int, index int) []int {
	if len(result) < index + 1 {
		return append(result, value)
	} else {
		result[index] = value
		return result
	}
}
