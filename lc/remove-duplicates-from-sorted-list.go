/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// d 1 -1 1 2 3 n
//   p-------
//           c
// so p moves only when they are not the same
// c always moves
// d 1 1 2
// d 1   2
//   --- p
//         c
func deleteDuplicates(head *ListNode) *ListNode {
    d := &ListNode {Val: -101, Next: head}
    p := d
    for c := head; c != nil; c = c.Next {
        if p.Val == c.Val { 
            p.Next = c.Next
        } else {
            p = c
        }
    }
    return d.Next
}