# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
create new list on the fly, stop
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l3 = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1val = l2val = 0
            if l1:
                l1val = l1.val
                l1 = l1.next
            if l2:
                l2val = l2.val
                l2 = l2.next
            trunc = (carry + l1val + l2val) % 10
            l3.next = ListNode(trunc)
            l3 = l3.next
            carry = (carry + l1val + l2val) // 10
        return head.next
