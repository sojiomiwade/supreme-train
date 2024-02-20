class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)

            5
           /  \
          6
           \
            7
            /
           2
          /
         3
        /

recursive func          
    if not node, return 
    if my idx is not in lookup:
        lookup[myidx]=node.val
        if my idx is smaller than parent's
            appendleft
        else (it is greater)
            appendright
    recurse(me.right,myidx,myidx+1)
    recurse(me.left,myidx,myidx+1)    

then just iterate the deque from the start
            5
          6
            7
lookup {50 -16}
ans [6 5]
root,rootidx,paridx=7,0,-1
"""
from collections import deque
def topView(root):
    def topview(root,rootidx,paridx):
        if root:
            if rootidx not in lookup:
                lookup[rootidx]=root.info
                if rootidx<paridx:
                    a.appendleft(root.info)
                else:
                    a.append(root.info)
            topview(root.left,rootidx-1,rootidx)
            topview(root.right,rootidx+1,rootidx)
        
    lookup={root:0}
    a=deque([root.info])
    topview(root.left,-1,0)
    topview(root.right,1,0)
    print(' '.join(str(val) for val in a))



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)