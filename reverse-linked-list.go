/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/*
x   1 > 2 > 3 > 4 > 5 > x
                        t    
                    c 
                p   
x < 1 < 2 < 3 < 4 < 5 > x
loop on as long as c is not nil
t holds c's next
current next points to prev
next it: pre moves to c, c moves to t
. > 1 > 2 > x
n < 1 < 2 > x
        p
            c
            t    

*/
func reverseList(head *ListNode) *ListNode {
    var p *ListNode
    c := head
    for ; c != nil; {
        t := c.Next
        c.Next = p
        p, c = c, t
    }
    return p
}