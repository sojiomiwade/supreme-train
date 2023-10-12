'''
Given a linked list node, a1 such that
a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
Weave this linked list so that it becomes
a1 -> b1 -> a2 -> b2 -> ... -> an -> bn 
'''
from __future__ import annotations
from types import resolve_bases
from typing import List, Optional

class Node:
    def __init__(
        self, 
        val: Optional[int]=None,
        nxt: Optional[Node]=None,
        ) -> None:
        self.val = val
        self.nxt = nxt

    def getlist(self) -> List[int]:
        res = []
        node = self
        while node:
            res += [node.val]
            node = node.nxt
        return res

    def insert_after_self(self, node: Node):
        self.nxt, node.nxt = node, self.nxt

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

    def weave2(self) -> None:
        tail_a = self.get_tail_a()
        a, b = self.nxt, tail_a.nxt
        tail_a.nxt = None
        curr = self
        while a:
            assert b

            curr.nxt = a
            curr = curr.nxt
            a = a.nxt
            
            curr.nxt = b
            curr = curr.nxt
            b = b.nxt
            

    def weave(self) -> None:
        tail_a = self.get_tail_a()
        # print(otherhead.val) # 4 
        a, b = self.nxt, tail_a.nxt
        tail_a.nxt = None
        while a:
            assert b
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
    return dhead

n = 10
dhead = init_list(n)
assert dhead.nxt
dhead.weave2()
reslist = dhead.nxt.getlist()
assert reslist == list(range(1,11))

