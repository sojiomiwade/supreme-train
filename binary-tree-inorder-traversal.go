/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// inoleft, print (node), ino right
// a = [1 3 2]
func inorderTraversal(root *TreeNode) []int {
    var ino func (root *TreeNode)
    a := []int{}
    ino = func (root *TreeNode) {
        if root != nil {
            ino(root.Left)
            a = append(a, root.Val)
            ino(root.Right)
        }
    }
    ino(root)
    return a
}