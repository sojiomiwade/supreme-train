# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
          1 
        /   \
       2     3
      / \   / \
     4   5 6   7
ans=4 5 2 6 7 3 1
root 5
st  1f 2t
popped = 2f
res 4
as long as there is root or stack
    if root is not null, 
        push onto the stack (root,false)
        set root to its left 
    else 
        pop (root,isready) from the stack
        if not ready 
            push (root,true) onto the stack
            root=root.right
        else
            process element
            root=null

             1
            / \
           2   3
ans 2 3 1
root n
st    
ready t
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st,ans=[],[]
        while root or st:
            if root:
                st.append((root,False))
                root=root.left
            else:
                root,ready=st.pop()
                if not ready:
                    st.append((root,True))
                    root=root.right
                else:
                    ans.append(root.val)
                    root=None
        return ans