'''
Given a linked list node, a1 such that
a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
Weave this linked list so that it becomes
a1 -> b1 -> a2 -> b2 -> ... -> an -> bn 

a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn

0 2 4 6 8 1 3 5 7 9
0 1 2 3 4 5 6 7 8 9

find the middle. it's next is b1
then point a1 to b1. and call weave on old a1.next and b1.next
then set  b1.next to the return of those two
at the end both params will be null (assert that)
0 1 --> (2,)
time,space=O(n),O(n)
time for optimal approach: 
'''
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional[Node]) -> None:
        self.val=val
        self.next=next

def findmid(a: Node) -> Node:
    # 0 1 2
    #   s
    #     f
    slow=fast=a
    while fast.next and fast.next.next:
        fast=fast.next.next
        assert slow.next
        slow=slow.next
    return slow

def weave(a: Optional[Node]) -> Optional[Node]:
    '''
     /---\
    0  2  1 3
    a  m  b
       t  
    0-> 1 --> weave(2,3)

    /---\
    2   3
    a   t
        b

    '''
    def weave(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        if not a:
            assert not b
            return None
        assert a and b
        temp=a.next
        a.next=b
        b.next=weave(temp,b.next)
        return a
    if not a:
        return None
    mid=findmid(a)
    b=mid.next
    mid.next=None
    assert b
    return weave(a,b)

