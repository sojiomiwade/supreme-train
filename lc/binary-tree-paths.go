/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func btp(root *TreeNode, buf []string, ans []string) []string {
    if root == nil {
        return ans
    }
    buf = append(buf, strconv.Itoa(root.Val))
    if root.Left == nil && root.Right == nil {
        s := strings.Join(buf, "->")
        fmt.Println(s)
        ans = append(ans, s)
    }
    ans = btp(root.Left,buf,ans)
    ans = btp(root.Right,buf,ans)
    buf = buf[:len(buf)-1]
    return ans
}
func binaryTreePaths(root *TreeNode) []string {
    return btp(root, []string {}, []string {})
}