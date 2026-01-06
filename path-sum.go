/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// dfs: if there is a sum, shore up that sum alone. 
// in main func, return true if helper val is the sum
// backtrack of course to correct the sum
//         5
//       /   \
//      4     8
// 13 -- true: 
// ts: 8
// 4 -- false
func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil { return false }
    targetSum -= root.Val
    if root.Left == nil && root.Right == nil {
        return targetSum == 0
    }
    return hasPathSum(root.Left, targetSum) || hasPathSum(root.Right, targetSum)
}