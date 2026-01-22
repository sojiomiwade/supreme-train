# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# recursively is easiest...
# 1 2 4
#       t
#       b
# 1 3 4 5 6 7
# d - 1 1 2 3 4 4 5

# 1
#   a
# b
# 2 3

# 1- 
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a and not b:
            return None
        if not a or not b:
            return a or b
        if a.val < b.val:
            a.next = self.mergeTwoLists(a.next, b)
            return a
        b.next = self.mergeTwoLists(a, b.next)
        return b
        
