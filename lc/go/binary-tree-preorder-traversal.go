/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// process root
// then left
// then right
// st []
// r 1 2 4 x 5 6 x 7 3 x
// ans [1]
// now iterative...
// with stack and root: 
// push your right before proceeding down to the left; done when no stack or root
//         1
//     3
//         2  
// 1 3 2 expected
// root x
// st []
// ans [1 3 2]

func preorderTraversal(root *TreeNode) []int {
    st, ans := []*TreeNode{}, []int{}
    for ; len(st) > 0 || root != nil; {
        if root != nil {
            ans = append(ans, root.Val)
            st = append(st, root.Right)
            root = root.Left
        } else {
            root = st[len(st) - 1]
            st = st[:len(st) - 1]
        }
    }
    return ans
}
