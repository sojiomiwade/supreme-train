/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// s(p, q)
// boundary conditions: 
//     one may be nil, and the other not. 
//     both nil is ok
// base case returns false when p and q are not the same
// recursive steps is simple: check left and right
    //     1           1
    //   /   \
    //  2     3       2     
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil && q == nil { return true }
    if p == nil || q == nil { return false }
    if p.Val != q.Val { return false }
    return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}