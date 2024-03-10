# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
       3
    /     \
   1      5 
    \    /  
    2   4
31254
        3
       /            \
      1 -i,3         5  (3,i)
       \            / \
        2 1,3      4 3,5
       / \    
serialize: preorder
deserialize: pass lb and ub beginningwith -inf,+inf
3
 1

'''
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        def ser(root: Optional[TreeNode]) -> str:
            if root:
                ans.append(str(root.val))
                ser(root.left)
                ser(root.right)
        ans=[]
        ser(root)
        return ' '.join(ans)

    '''
    3
     \
      5
    ans [3 5] -> "3 5"
    deser:
    vals []
        3
       /       \ 
      N(min,3)  5  (3,max)  
    '''
    def deserialize(self, data: str) -> Optional[TreeNode]:
        MINBOUND,MAXBOUND=-1,10001
        def deser(lb: int, ub: int) -> Optional[TreeNode]:
            if vals and lb<int(vals[0])<ub:
                root=TreeNode(int(vals.popleft()))
                root.left=deser(lb,root.val)
                root.right=deser(root.val,ub)
                return root
            return None
 
        vals=deque(data.split())
        return deser(MINBOUND,MAXBOUND)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans