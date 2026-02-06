/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//   9 9 9 3 2 6 4 1 8 4 5
//         i
//         j       
//   3 5 6 1 8 4 5

// sweep through headA and keep all in a hashmap
// then sweep through headB until you find something in the map... thats your answer!
// time: O(m + n)
// space: O(min(m,n))
// heada 1 2 3
// headb 2 3

// 1. reverse the two lists!
// 2. then find *last* common node
// 3. then reverse both lists back!
// 4. return last
// complexity: same as before but space is constant now!

// have = {1n 2n 3n}
//     1 > 2 > 3 > 4 > x
// d < 1 < 2 < 3   x
//             p   
//                 c
//                 t
// 2 5
// 5
// 5 2
// 5
func reverse(h *ListNode) *ListNode {
    var p *ListNode = nil
    for t,c := h,h; c != nil; {
        t = t.Next
        c.Next = p
        p, c = c, t
    }
    return p
}

func findlast(a, b *ListNode) *ListNode {
    var p *ListNode = nil
    for ca, cb := a, b; ca != nil && cb != nil && ca == cb ; ca, cb = ca.Next, cb.Next {
        p = ca
    }
    return p
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
    ra, rb := reverse(headA), reverse(headB)
    ans := findlast(ra, rb)
    reverse(ra)
    reverse(rb)
    return ans
}