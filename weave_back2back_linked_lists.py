'''
Given a linked list node, a1 such that
a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
Weave this linked list so that it becomes
a1 -> b1 -> a2 -> b2 -> ... -> an -> bn 
'''
from __future__ import annotations
from typing import Optional

class Node:
    def __init__(
        self, 
        val: Optional[int]=None,
        nxt: Optional[Node]=None,
        ) -> None:
        self.val = val
        self.nxt = nxt

    def print_list(self):
        node = self
        while node:
            print(node.val, end=', ')
            node = node.nxt
        print()

    '''
    2 insertafter y
    2->x
    2 -> y -> x

     = y,x
    '''
    def insert_after_self(self, node: Node):
        self.nxt, node.nxt = node, self.nxt

    '''
    1 2

    1 2 3 4
        f
      s
    '''
    def get_tail_a(self) -> Node:
        pslow = pfast = self
        while pfast and pfast.nxt and pfast.nxt.nxt:
            pfast = pfast.nxt
            assert pfast
            pfast = pfast.nxt
            assert pslow
            pslow = pslow.nxt
        assert pslow
        return pslow
    '''
    1 2 3 4 5 6 x
    a c   b d 
    
    1 4 2 3 4...   5 6 x  
        a c        b d

    1 4 2 5 3 4 6 x
            a c b d

    1 4 2 5 3 6 4 x
                a b  
    '''
    def weave(self) -> None:
        tail_a = self.get_tail_a()
        # print(otherhead.val) # 4 
        a, b = head, tail_a.nxt
        tail_a.nxt = None
        while a and b:
            c, d = a.nxt, b.nxt
            a.nxt, b.nxt = b, c
            a, b = c, d
        

def init_list(n: int) -> Node:
    dhead = Node()
    for i in range(n, 0, -2):
        dhead.insert_after_self(Node(i))
    for i in range(n-1, 0, -2):
        dhead.insert_after_self(Node(i))
    assert dhead.nxt
    return dhead.nxt
head = init_list(10)
head.print_list() # 1 2 3 4 5 6
head.weave()
head.print_list() # 1 4 2 5 3 6

