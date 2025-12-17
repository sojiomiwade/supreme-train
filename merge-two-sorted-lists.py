/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 1 2 4
   ^
 1 3 4
 ^

loop until a and b are both nil
    aval = bval = 101
    reset them if the node vals if not nil
    if aval < bval
        r.next = a
        a = a.next
    else 
        r.next = b
        b = b.next

 return r

 1
 2
 av bv = 1 2
 r = (0) -> 1
 */
func mergeTwoLists(a *ListNode, b *ListNode) *ListNode {
    r := &ListNode{}
    rr := r
    inf := math.MaxInt
    for ; a != nil || b != nil; r = r.Next {
        aval, bval := inf, inf
        if a != nil {aval = a.Val}
        if b != nil {bval = b.Val}
        if aval < bval {
            r.Next = a
            a = a.Next
        } else {
            r.Next = b
            b = b.Next
        }
    }
    return rr.Next
}
