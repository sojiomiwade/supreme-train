/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// bfs approach: at each pop, 
// check target - rootval
// on next row of bfs

// while q has elements
// on pop, if node is leaf and nodeval - target is 0, return true
// for each child, push (child, target - root) to queue
// return false
//             5
//          4     8
// t 13
// q = [(8,8)]
// head = (9, 4)
        //      1
        //     / \
        //    2   3
func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil { return false }
    type pair struct{t int; node *TreeNode}
    q := []pair{pair{t: targetSum, node: root}}
    for ; len(q) > 0; {
        head := q[0]
        q = q[1:]
        if head.node.Left == nil && head.node.Right == nil && head.t == head.node.Val {
            return true
        }
        
        if head.node.Left != nil {
            q = append(q, pair{head.t - head.node.Val, head.node.Left})
        }
        if head.node.Right != nil {
            q = append(q, pair{head.t - head.node.Val, head.node.Right})
        }
    }
    return false
}