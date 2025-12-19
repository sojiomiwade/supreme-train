# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
runner technique
1 2 3
  s
    f
if f has a next return s.next. otherwise return s

1
s
f

1 2 3
  s
    f
return 2
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
