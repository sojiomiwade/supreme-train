/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    cur := head
    for cur != nil {
        for cur.Next != nil && cur.Next.Val == cur.Val { cur.Next = cur.Next.Next } 
        cur = cur.Next
    }
    return head
}