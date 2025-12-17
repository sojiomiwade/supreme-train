'''
Leetcode 129: Sum root to leaf numbers.

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

                1
            2       5
                     
        5     7   8   

    (125, 127, 158)

fallback: keep a list of numbers: space: O(n)
better: time : O(n), space: O(h)
idea: 
    + if no child, make number; 
    + if you have child, visit that child after appending selve
    + if leaf, sum += buf
    + at end remove yourself
'''
from typing import Optional,List

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

'''
'''
def sumpaths(root: Optional[Node], buf: List[str]) -> int:
    if not root:
        return 0
    assert root
    buf.append(str(root.val))
    if not root.left and not root.right:
        val=int(''.join(buf))
    else:
        val=sumpaths(root.left,buf)+sumpaths(root.right,buf)
    buf.pop()
    return val

'''
a = a * 10 + val
 
                1
            2       5
              7   
            127 + 15
buf []
root  1
val 127 + 15 = 142

                1
            2       5
                     
        5     7   8   
125+127+158
'''

root=None
print(sumpaths(root,[])) #0
root=Node(1, Node(2,None,Node(7)), Node(5))
print(sumpaths(root,[])) # 142
root=Node(1, Node(2,Node(5),Node(7)), Node(5,Node(8)))
print(sumpaths(root,[])) # 410
root=Node(1, Node(2,Node(5),None), None)
print(sumpaths(root,[])) # 125
