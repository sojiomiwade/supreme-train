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

root can be seen
root calls right and left  with seen=true
if i am a left (i pass true to left and false to right)
if i am a right(vice versa)

     1
  /    \
 5      2
  \    /  \
  8    1  5
  /      /  \
 1      3    6
      \
       4- ...    - 7

if curidx > ridx then append to ans, the value of root. set ll[curidx]=curlevel
elif curidx < lidx then append left to ans, the value of root. set ll[curidx]=curlevel
elif cur_level is higher than ll[curidx], ignore
else (cur level is lower than ll[curidx]), ans[curidx]=root.val
   1
 /   \
4    2
    /
   3
expected ans 4 1 2
          v
 ans [0 4 1 2 0 0] offset = 2
      0 1 2 3 4 5
ll {00 -11}
lidx,ridx -1,1
root,idx,level 3 0 2
"""
def topView(root):
    def topview(root,idx,level) -> None:
        nonlocal lidx,ridx
        if not root:
            return
        if not lidx<=idx<=ridx or level<ll[idx]:
            ans[idx+offset]=root.info
            ll[idx]=level
            ridx=max(ridx,idx)
            lidx=min(lidx,idx)
        topview(root.left,idx-1,1+level)
        topview(root.right,idx+1,1+level)
                        
    ll={}
    MAX=1000; INF=MAX; lidx,ridx=INF,-INF; offset=499
    ans=[0 for _ in range(MAX)]
    topview(root,0,0)
    for idx in range(lidx,ridx+1):
        print(ans[idx+offset],end=' ')
    print()
    


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)