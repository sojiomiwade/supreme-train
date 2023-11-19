# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
               8
             /   \
            2     5
           /       \
          3         8
        823### 5#8##
        8
      2.   5
    3.       8     
'''
class Codec:

    def serialize(self, root):
        def preorder(root):
            if not root:
                prel.append('#')
            else:
                prel.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        prel = []
        preorder(root)
        return ' '.join(prel)

    def deserialize(self, data):
        '''
               8
                 \
                  5
                   \
                    8
        8#5#8##
                    8
                n       5
                      n   8
                         n.  n
        '''
        def _deser():
            val = next(vals)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = _deser()
            root.right = _deser()
            return root
        vals = iter(data.split())
        return _deser()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def ser(root, l):
            if root:
                l.append(str(root.val))
                ser(root.left,l)
                ser(root.right,l)
            else:
                l.append('#')
            return l

        return ' '.join(ser(root,[]))        

    def deserialize(self, data):
        def deser():
            r=None
            x=q.popleft()
            if x!='#':
                r=TreeNode(int(x))
                r.left=deser()
                r.right=deser()
            return r

        q=deque(data.split())
        return deser()        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))