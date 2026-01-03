/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//  bfs or dfs would solve this
//  dfs is simplest: 
// if nil, return 0
// otherwise return 1 + max(maxDepth(left), maxD(right))
//     1
//   2   x
// 2: l, r = 0
func maxDepth(root *TreeNode) int {
    if root == nil { return 0 }
    left := maxDepth(root.Left)
    right := maxDepth(root.Right)
    if right > left { return 1 + right}
    return 1 + left
}