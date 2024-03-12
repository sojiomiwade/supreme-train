# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
d                                 h
.-->---------------->------------->
0  1, 3, 2, -3, -2, 5, 100, -100, 1
   1  4  6   3,  1, 6, 106,    6, 7
prefix 6
0, 1
lin {0:d 4:3 3:-3 1:-2 106:100 6:-100 7:1}
lipn means last (including this node) identity node having same prefix
0 3 1 -1 n
  3 4  3
0:d 3:-1
'''
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prefix=0
        lipn={0:dummy}
        while head:
            prefix+=head.val
            lipn[prefix]=head
            head=head.next
        head=dummy
        prefix=0
        while head:
            prefix+=head.val
            head.next=lipn[prefix].next
            head=head.next
        return dummy.next