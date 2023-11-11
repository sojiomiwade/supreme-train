# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
             2
            / \
           1   3
        pre [213]
        ino []
        '''
        def preorder(root, pre):
            if root:
                pre.append(str(root.val))
                preorder(root.left,pre)
                preorder(root.right,pre)
            return pre

        def inorder(root,ino):
            if root:
                inorder(root.left,ino)
                ino.append(str(root.val))
                inorder(root.right,ino)
            return ino

        pre=preorder(root,[])
        ino=inorder(root,[])
        return ','.join(pre) + '-' + ','.join(ino)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
        pre [2, 1] 
        ino [1, 2] 
        iil {1: 0, 2: 1}
        lo hi 01, 11, 11 
        TN(2, TN(1,n,))
        mi 0
        '''
        def _deserialize(lo,hi,nextpre):
            if lo > hi:
                return None,nextpre
            print(lo, hi, nextpre)
            root = TreeNode(pre[nextpre])
            nextpre += 1
            mi = iil[root.val]
            root.left,nextpre = _deserialize(lo,mi-1,nextpre)
            root.right,nextpre = _deserialize(mi+1,hi,nextpre)
            return root,nextpre

        if data == '-':
            return None
        pres, inos = data.split('-')
        print(data)
        pre = [int(x) for x in pres.split(',')]
        ino = [int(x) for x in inos.split(',')]
        iil = {ino[i]:i for i in range(len(ino))}
        print(pre,ino,iil)
        return _deserialize(0, len(pre)-1, 0)[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans