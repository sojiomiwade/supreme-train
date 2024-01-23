'''
return k-th to last element in a list
k=3
0 1 2 3 4 5 6 
8 1 5 3 0 2 9 n
      s
            f
ans_idx=4
n=7
k=3=>
mid=
mi  ...  -3 -2  n-1
---------|---------
n-1-mi-k       3
6-3-3=0
move 0 and return the next

try for 5
6-3-2=1
move 1, and return the next!


now what if number of elements is even
. 0 1 2 3 4 5  6  7
  8 1 5 3 0 2 (9) 2 n
  s
    f
do not move fast if double hope lands it on null
k=2
7-3-2=2
so move 2 and return next, it works!
k=8
7-3-8=-4

if -ve move -4+mi+1 from head instead
-3+mi+1 = 1 it works

if -ve, move -moves+mi+1 from head instead, and return *that* node, not the next
'''
from typing import List, Optional


class Node:
    def __init__(self,val,next) -> None:
        self.val=val
        self.next=next

def k2last(head: Optional[Node], k: int) -> Node:
    # 1 2 n
    def findmid():
        assert head
        slow=fast=head
        n=1
        mi=0
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            n+=2
            mi+=1
        print(n+bool(fast.next),mi,slow.val)
        return n+bool(fast.next),mi,slow

    ''''
    0 1 2 3 4 5 6 7 8 
            m=4     k=1
                    n-k=9-1=8 => 8-4
    0 1 2 3 4 5 6 7 8 9 
            m=4     k=2
                    n-k=8 moves from head
n-k-m from m if n-k>=m
otherwise just use n-k
8-4=4
    we need idx
     ---------|-----mi
             n-k
    0 1 2 3  [4] 5 6 7  8  9
    8,1,5,3, 0,  2,9,11,12,13, k=6
    s
    f
      wrong
            right
    10,4,0
    moves=9-4-6=-1
    '''
    assert head
    n,mi,midnode=findmid()
    assert 1<=k<=n
    if n-k>=mi:
        for _ in range(n-k-mi):
            midnode=midnode.next
        assert midnode
        return midnode
    for _ in range(n-k):
        head=head.next
    assert head
    return head

#even count
#8 1 5 3 0 2 (9) 2 n, k=2
def makenode(idx: int, arr: List[int]) -> Optional[Node]:
    if idx==len(arr):
        return None
    return Node(arr[idx],makenode(idx+1,arr))

def printnodes(head: Optional[Node]) -> None:
    while head:
        print(head.val,end=',')
        head=head.next
    print()

head=makenode(0,[8,1,5,3,0,2,9,2])
printnodes(head)
print(k2last(head,k=2).val) # 9

head=makenode(0,[8,1,5,3,0,2,9])
printnodes(head)
print(k2last(head,k=2).val) # 2

head=makenode(0,[8,1,5,3,0,2,9,11,12,13])
printnodes(head)
print(k2last(head,k=6).val) # 3

head=makenode(0,[8,1,5,3,0,2,9,2])
printnodes(head)
print(k2last(head,k=6).val) # 5
