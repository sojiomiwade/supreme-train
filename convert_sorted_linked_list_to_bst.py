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
0 1 2 3 4 5 6 7 n
            f
      s
0 1 2 3 4 5 6 n
            f
      s
0 1 2 3 [4]
         f
    s

func l2bst(lo,exhi) <---exclusive
    terminate: lo==exhi...yes
    return None
    otherwise get mid and make it the head
    then call (for tree-left and tree-right) ll2bst(lo,mid) and ll2bst(mid.next,exhi)
    return root
time: n lg n
space: 1
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def ll2bst(lo,exhi):
            if lo is exhi:
                return None
            slow=fast=lo
            while fast and fast.next and exhi not in (fast,fast.next):
                fast=fast.next.next
                slow=slow.next
            root=TreeNode(slow.val)
            root.left=ll2bst(lo,slow)
            root.right=ll2bst(slow.next,exhi)
            return root
        return ll2bst(head,None)