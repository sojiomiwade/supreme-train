/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type pair struct {
    node *TreeNode
    path []string
}
/*
            1
          /    \
         2      3
          \    /
           5  6
        ans: 125, 136
*/
func binaryTreePaths(root *TreeNode) []string {
    q := []pair {pair{root,[]string{strconv.Itoa(root.Val)}}}
    ans := []string {}
    for ; len(q) > 0; {
        pr := q[len(q)-1]
        q = q[:len(q)-1]
        root, rootpath := pr.node, pr.path
        if root.Left == nil && root.Right == nil {
            ans = append(ans, strings.Join(rootpath, "->"))
        } else {
            if root.Left != nil {
                leftpath := append([]string{}, rootpath...)
                copy(leftpath, rootpath)
                leftpath = append(leftpath, strconv.Itoa(root.Left.Val))
                lpr := pair {root.Left, leftpath}
                q = append(q, lpr)
            }
            if root.Right != nil {
                rightpath := append([]string{}, rootpath...)
                rightpath = append(rightpath, strconv.Itoa(root.Right.Val))
                rpr := pair {root.Right, rightpath}
                q = append(q, rpr)
            }
        }
    }
    return ans
}