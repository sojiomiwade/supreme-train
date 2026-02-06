/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// 0 nodes = 0
// 1 node = 1
// and so on. 
// so bottom-up: min of left and right is 1 + the min you can get
func minDepth(root *TreeNode) int {
    if root == nil { return 0 }
    if root.Left != nil && root.Right != nil {
        return 1 + min(minDepth(root.Left), minDepth(root.Right))
    }
    return 1 + max(minDepth(root.Left), minDepth(root.Right))
}