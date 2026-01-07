# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2 4 3
# 5 6 4
# 7 0 8
# as long as there's carry or t or b, we loop
#       4 
#         l1
#           l2
#       9 1
#         c
#       3 2 <-- exp
# ans-> 3 -> 2 -> 
# c 0
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        cur = ans = ListNode()
        while c or l1 or l2:
            if l1:
                c += l1.val
                l1 = l1.next
            if l2:
                c += l2.val
                l2 = l2.next
            cur.next = ListNode(c % 10)
            cur = cur.next
            c //= 10
        return ans.next