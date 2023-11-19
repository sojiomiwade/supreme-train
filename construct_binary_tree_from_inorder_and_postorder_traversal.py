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

po=
ill={50,81,32}
                                02(5,0)
                      0-1(null)                          12(3,2)
                                                 11(8,1)                   32
                                            10            21
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTree(lo,hi):
            r=None
            if lo<=hi:
                r=TreeNode(po.pop())
                mi=ill[r.val]
                r.right=buildTree(mi+1,hi)
                r.left=buildTree(lo,mi-1)
            return r
        ill={ival:i for i,ival in enumerate(inorder)}
        po=postorder[:]
        return buildTree(0,len(inorder)-1)