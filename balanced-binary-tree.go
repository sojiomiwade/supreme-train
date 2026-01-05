/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// left depth - right depth cannot differ by more than one!
// nil - depth is zero

//  1 
// 2 3
//      4
//         5
// should be true
// 1 + 1 + 1 + 
// dep(4)
// 2 -- 1
// 3 -- 3
// 1 - 3 == -2
// 1
//  2
//    3
// 1: ld: 0, rd: 
// 2: 
// 3: 
func dep(root *TreeNode) (int, bool) {
    if root == nil { return 0, true }
    ld, lans := dep(root.Left)
    rd, rans := dep(root.Right)
    val := ld - rd
    val = max(val, -val)
    return 1 + max(ld, rd), val < 2 && lans && rans
}

func isBalanced(root *TreeNode) bool {
    _, ans := dep(root)
    return ans
}