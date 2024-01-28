# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev=float('-inf')
        st=[]
        while st or root:
            if root:
                st.append(root)
                root=root.left
            else:
                next=st.pop()
                if prev<next.val:
                    prev=next.val
                else:
                    return False
                root=next.right
        return True
