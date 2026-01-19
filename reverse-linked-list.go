/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/*
1 > 2 > 3 > 4 > 5 > x
1 < 2.< 3.< 4.< 5.  x
on come back of recursive function, 
have next point at you, then return what was returned!

h
c
c
1 > 2 > 3 > x
1 < 2 < 3 
a:3

1 > 2
*/
func rl(head *ListNode) *ListNode {
    if head.Next == nil {
        return head
    }
    ans := rl(head.Next)
    head.Next.Next = head
    return ans
}

func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    ans := rl(head)
    head.Next = nil
    return ans
}