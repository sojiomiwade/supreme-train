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
arr=list_to_arr()
1 2 3 4 5 6 7 8
            4
        1,3->2      5-8 -> 6
      1  3
time: O(n)
space: O(n)
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def ll2arr(head):
            arr=[]
            while head:
                arr.append(head.val)
                head=head.next
            return arr

        def arr_to_bst(lo,hi):
            if lo>hi:
                return None
            mi=lo+(hi-lo)//2
            root=TreeNode(arr[mi])
            root.left=arr_to_bst(lo,mi-1)
            root.right=arr_to_bst(mi+1,hi)
            return root

        arr=ll2arr(head)
        return arr_to_bst(0,len(arr)-1)