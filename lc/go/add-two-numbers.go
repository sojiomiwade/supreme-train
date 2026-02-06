/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//   2 4 3
//   5 6 4
// h 7 0 8
// h c
// always 3 things top bot car
// make a new node until top bot and car are all 0
// use a do-while, so you go the 1st time
//  8 
//  5
// h {0} -> {3} -> {1}
// car 1
// top bot val 0 0 1
// l1 l2 nil nil
// cur {1}
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    h, car := &ListNode{}, 0
    cur := h
    for ; car != 0 || l1 != nil || l2 != nil ; {
        top, bot := 0, 0
        if l1 != nil {
            top = l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            bot = l2.Val
            l2 = l2.Next
        }
        val := (car + top + bot) % 10
        cur.Next = &ListNode{Val: val}
        cur = cur.Next
        car = (car + top + bot) / 10
    }
    return h.Next
}