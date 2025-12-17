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
abcdn
  s
    f
landing on null ok, but can't go past it
complexity n lg n
r(head, none)
get the middle make it root
set root.left to recurse(head to me), set root.right to r(me.next to right)
l,r = -10 0
m=-3
r(-10,-3)
r(0,0)
if the left is right, no range and can return
range for -3 is ()
1 3
  f
s
since the tail is not inclusive, then if f senses the end, s must not move
can't go beyond the terminal!
so if next or next.next is the terminal, then end
1 2 3
  s
    f
               0
            /     \
           -10     5
             \      \
             -3      9
0 1 2 n
s
f
mid 1

     1
   /   \
  0
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findmid(start, term):
            slow=fast=start
            while fast is not term and fast.next is not term:
                fast=fast.next.next
                slow=slow.next
            return slow

        def list2bst(head, term):
            if head is term:
                return None
            mid=findmid(head,term)
            root=TreeNode(mid.val)
            root.left=list2bst(head,mid)
            root.right=list2bst(mid.next,term)
            return root

        return list2bst(head,None)