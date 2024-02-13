# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1 2 3 4 5
  s
    f
return slow
mid find the mid (not prev)
make it root.
call convert to (head,mid) and (mid.next,tail) <--tail is exclusive
return root

1 t
s
f

h t
h,h -- t,t
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findmid(head,tail):
            slow=fast=head
            while fast.next is not tail and fast.next.next is not tail:
                fast=fast.next.next
                slow=slow.next
            return slow

        def convert(head,tail):
            if head is tail:
                return None
            mid=findmid(head,tail)
            return TreeNode(mid.val,convert(head,mid),convert(mid.next,tail))

        return convert(head,None)