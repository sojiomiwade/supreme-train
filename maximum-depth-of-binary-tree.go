/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// this time let's use bfs
// keep track of max level
// if next level stack is empty, we are done
// at top of while, if stack has something, increment ans
// at the end, return ans
//      1
//    2   x
// ans 2
// a []
// b
// n 2
func maxDepth(root *TreeNode) int {
    ans := 0
    if root == nil { return 0 }
    a := []*TreeNode{root}
    for ; len(a) > 0; {
        ans += 1
        b := []*TreeNode{}
        for _,n := range a {
            if n.Left != nil {b = append(b, n.Left)}
            if n.Right != nil {b = append(b, n.Right)}
        }
        a = b
    }
    return ans
}