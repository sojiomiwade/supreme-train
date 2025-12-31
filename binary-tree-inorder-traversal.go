/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// 1 
//  \
//   2
//  /
// 3
// ans = [1 3 2]
// need st for saving r, to process left first. 
// as we loop, st tells us if there a saved. 
// r nil means no left, so pop for saved. if cant pop either we are done
// if r defined, push it, and set r to r.left
// otherwise, pop and print, then set r to the right 
// 1 
//   2
// expected ans = [1 2]
// ans = [1]
// s = [2]
// root = 2
// slen = 1
func inorderTraversal(root *TreeNode) []int {
    s := []*TreeNode{}
    a := []int{}
    for len(s) > 0 || root != nil {
        if root != nil {
            s = append(s, root)
            root = root.Left
        } else {
            slen := len(s)
            root = s[slen - 1]
            s = s[:slen-1]
            a = append(a, root.Val)
            root = root.Right
        }
    }
    return a
}