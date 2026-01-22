/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
/*
        4
dfs: do swap left and right, and recurse on each one
bfs: iterate through q (or stack) swapping left and right. dont put nil in st
        1
    2-3       3-2
                   4
3 2

            1
             \
               2
             /
            3

st  []  
top 3
            1
            /
           2
            \
             3
*/
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    st := []*TreeNode {root}
    for ; len(st) > 0; {
        top := st[len(st)-1]
        st = st[:len(st)-1]
        top.Left, top.Right = top.Right, top.Left
        if top.Left != nil {
            st = append(st, top.Left) 
        }
        if top.Right != nil {
            st = append(st, top.Right) 
        }
    }
    return root
    // if root == nil {
    //     return nil
    // }
    // root.Left, root.Right = invertTree(root.Right), invertTree(root.Left)
    // return root
}