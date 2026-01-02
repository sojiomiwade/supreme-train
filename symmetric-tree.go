/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//  left and right
// bfs where the queue is equal to its reverse for each row
// dfs: ...
// preorder equals postorder is the guaranteed way to solve this -- fail
//     1
//    2   x
// q = [2, x]
// ch = [2, x]
func reverses(a []*TreeNode) bool {
    n:=len(a)
    for i,j:=0,n-1; i<j; i,j=i+1,j-1 {
        aival, ajval := 101, 101
        if a[i] != nil { aival = a[i].Val }
        if a[j] != nil { ajval = a[j].Val }
        if aival != ajval { return false }
    }
    return true
}
func isSymmetric(root *TreeNode) bool {
    q := []*TreeNode{root}
    for ; len(q) > 0; {
        if !reverses(q) { return false }
        ch := []*TreeNode{}
        for _,n := range q {
            if n == nil { continue } 
            ch = append(ch, n.Left)
            ch = append(ch, n.Right)
        }
        q = ch
    }
    return true
}