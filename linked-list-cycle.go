/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// 1 2 1
//     c 
// nodes [1n, 2n]
func hasCycle(head *ListNode) bool {
    nodes := map[*ListNode]struct{} {}
    for curr := head; curr != nil; curr = curr.Next {
        if _, ok := nodes[curr]; ok { return true }
        nodes[curr] = struct{}{}
    } 
    return false
}