# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
oh
1 2 3
    h
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        orighead=head
        while head:
            while head.next and head.next.val==head.val:
                head.next=head.next.next
            head=head.next
        return orighead