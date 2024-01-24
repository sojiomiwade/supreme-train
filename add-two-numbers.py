# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
handle carry! 
    1
  3 4
  8 '0'
h 1 5  
  c
ans should be 1 5
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=cur=None
        carry=0
        while l1 or l2 or carry:
            l1val=0
            if l1:
                l1val=l1.val 
                l1=l1.next
            l2val=0
            if l2:
                l2val=l2.val 
                l2=l2.next
            digit=(l1val+l2val+carry)%10
            carry=(l1val+l2val+carry)//10
            if not cur:
                head=cur=ListNode(digit)
            else:
                cur.next=ListNode(digit)
                cur=cur.next
        return head