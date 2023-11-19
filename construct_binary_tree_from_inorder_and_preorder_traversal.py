# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            5
                3
              8
        ill={5:0,8:1,3:2}
        p=38
        mi=2

                02(5)
    0-1(null)            12(3)
                   11(8)         32(null)
             10(null)      21(null)
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTree(lo,hi):
            r=None
            if lo<=hi:
                r=TreeNode(p.popleft())
                mi=ill[r.val]
                r.left=buildTree(lo,mi-1)
                r.right=buildTree(mi+1,hi)
            return r
        p=deque(preorder)
        ill={ival:i for i,ival in enumerate(inorder)}
        return buildTree(0,len(preorder)-1)