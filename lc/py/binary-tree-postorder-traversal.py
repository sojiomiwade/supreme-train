# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# s [1 3]
# r 
# a, l [4 6 7 5 2], 2

# assuming root or stack:
# s []
# x 1
# lp 1
# a [2 3 1]
# r 
# lastp = null
# keep looping as long as root or st
# if root
#     push it on stack
#     root = root.left
# else:
#     x = peek at stack
#     if no right or x.right is lastp:
#         x <-- pop
#         append x.val to ans
#         lastp <-- x
#     else: #right and x.right is not lastp
#         root = x.right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st, lastp, ans = [], None, []
        while root or st:
            if root:
                st.append(root)
                root = root.left
            else:
                x = st[-1]
                if not x.right or x.right == lastp:
                    x = st.pop()
                    ans.append(x.val)
                    lastp = x
                else:
                    root = x.right
        return ans