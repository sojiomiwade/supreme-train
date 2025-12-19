# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1 2 3 4 5 6
call recursively passing the range of elements 
if range is defined, can create a node. otherwise return false
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def satb(left: int, right: int) -> Optional[TreeNode]:
            if left>right:
                return None
            mid=left+(right-left)//2
            root=TreeNode(nums[mid])
            root.left=satb(left,mid-1)
            root.right=satb(mid+1,right)
            return root
            
        n=len(nums)
        return satb(0,n-1)