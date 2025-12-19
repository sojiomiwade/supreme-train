# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
  -----
  V   ^
3 2 0 4
      s
      f

-----
1 2 3
s    
f  
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                return True
        return False