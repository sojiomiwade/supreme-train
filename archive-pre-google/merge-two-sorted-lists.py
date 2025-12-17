# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
ch

        l2  
 1   8  95 100
 
 58  93 94
           l1
         c


       l2
h-1  2 4
  V /| |
  1  3-4
       c  l1
if l1 > l2, then swap l1 and l2
cur points to l1, l1 advances to its next
cur advances to its next
at the end cur can just point to l1 or l2
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2=list1,list2
        head=cur=ListNode(0)
        while l1 and l2:
            if l1.val>l2.val:
                l1,l2=l2,l1
            cur.next=l1
            cur=cur.next
            l1=l1.next
        cur.next=l2 or l1
        return head.next