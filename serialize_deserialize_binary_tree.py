# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
12nn34nn5nn
        1
     /     \
    2
do()
    if top is null return that
    otherwise. 
    pop and make root
    root.left = do()
    root.right=do()
'''
class Codec:

    def serialize(self, root):
        def ser(root):
            if not root:
                ans.append('N')
            else:
                ans.append(str(root.val))
                ser(root.left)
                ser(root.right)
        ans=[]
        ser(root)
        return ' '.join(ans)

    '''
     3 
      5
       6
    ans1 3n5n6nn
    ans2: nn
       3
    /     \
   n       5
         /   \
        n     6
              n n
    '''
    def deserialize(self, data):
        def deser():
            val=vals.popleft()
            if val=='N':
                return None
            root=TreeNode(val)
            root.left=deser()
            root.right=deser()
            return root

        vals=deque([item for item in data.split()])
        ans=deser()
        assert not vals
        return ans

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))