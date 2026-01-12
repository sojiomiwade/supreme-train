/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//  3 2 0 4 8  7
//  ^         /
//   \       /
//     -----
// if we had 2 pointers, fast would reach nil, before slow
// otherwise fast will hit slow

// 1 2 3
//     s
//     f

// 1 2 3 4
//   s
//       f

// 1 2 3 4
// 2 4 2 4

// 1 2 3 4 5 6 7 8
// 2 4 6 8 2 4 6 8

// 1 2 3 4 5 6 7 
// 2 4 6 1 3 5 7

// 1
// s
// f

// check: is fast next slow?
// start fast at head.next, and slow at head
// loop until fast gets to end (careful it may not be able to move 2ce); return false if this happens
// if fa
// 1 2 3
//   s
//       f
func hasCycle(head *ListNode) bool {
    if head == nil { return false }
    slow, fast := head, head.Next
    for ; ; {
        if fast == slow { return true }
        if fast == nil || fast.Next == nil { break }
        slow, fast = slow.Next, fast.Next.Next
    }
    return false
}