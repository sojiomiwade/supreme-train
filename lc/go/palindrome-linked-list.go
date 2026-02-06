/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 1 2 3 4 3 2 1
 1 2 3 
 4 
 1 2 3
 s
         s
 could spit the elements out into array, and see if it is the reverse
 of itself wrt value ...
 cost: time, space:  O(n), O(n)
 1 2 1
 */
func isPalindrome(head *ListNode) bool {
    buf := []int{}
    cur := head
    for ; cur != nil; {
        buf = append(buf, cur.Val)
        cur = cur.Next
    }   
    for l,r := 0,len(buf)-1; l<r; l,r=l+1,r-1 {
        if buf[l] != buf[r] {
            return false
        }
    }
    return true
}