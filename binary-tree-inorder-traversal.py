# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
exp 2 4 1 5 3
           1
        /     \
       2       3
        \     /
         4   5
root 1
stack []
ans [2 4 1 5 3] 

1: root keeps going left filling the stack
on no val: pop stack into ans, and assign root to the right
back to 1 as long as there's root or stack

root traverses and fills stack
stack always gets the next element

1 
 \
  2         --> [1 3 2]
 /
3 
root n
top 2
st []
ans [132]
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st,ans=[],[]
        while root or st:
            while root:
                st.append(root)
                root=root.left
            top=st.pop()
            ans.append(top.val)
            if top.right:
                root=top.right
        return ans