# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1 2 3 4 5
        3
    2       4
  1            5
approach: 
def maketree(lo,hi)
    ...
return maketree(0,n-1)
1 2 3
    2
  1    3
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def maketree(lo: int, hi: int) -> Optional[TreeNode]:
            if lo>hi:
                return None
            mi=lo+(hi-lo)//2
            root=TreeNode(nums[mi])
            root.left=maketree(lo,mi-1)
            root.right=maketree(mi+1,hi)
            return root
        return maketree(0,len(nums)-1)