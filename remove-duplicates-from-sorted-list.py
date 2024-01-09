# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
one loop to advance the linked list, 
another on the inside to remove duplicates
    inner loop will 'remove' next as long as it is the same as cur
    ensure to check if next is null (no removal)
1 1 1 n
c--->        
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head