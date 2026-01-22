/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// recursion: take the middle, call conv on both sides
// if no interval, return nil
// 1 3
// 0 1

// lo hi mi  1 1 1 
//       1
//     /    \
//   nil.    3
func conv(nums []int, lo, hi int) *TreeNode {
    if lo > hi { return nil }
    mi := lo + (hi - lo)/2
    root := &TreeNode{Val: nums[mi]}
    root.Left = conv(nums, lo, mi - 1)
    root.Right = conv(nums, mi + 1, hi)
    return root
}
func sortedArrayToBST(nums []int) *TreeNode {
    return conv(nums, 0, len(nums) - 1)
}