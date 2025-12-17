# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4 5 n
prev = null
for node not null
    store node's next in temp
    node sets next to prev
    prev=node
    set node to temp
return prev
n<1<2<3 n
        h
      p
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        while head:
            nextnode=head.next
            head.next=prev
            prev=head
            head=nextnode
        return prev