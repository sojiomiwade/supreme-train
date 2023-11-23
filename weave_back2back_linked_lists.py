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

    def getlist(self, node: Optional[Node]) -> List[int]:
        res = []
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
        a, b = self.nxt, tail_a.nxt
        tail_a.nxt = None
        while a:
            assert b
            c, d = a.nxt, b.nxt
            a.nxt, b.nxt = b, c
            a, b = c, d
        
    def weave_recursive(self) -> None:
        def merge(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
            if not a:
                assert not b
                return None
            assert b
            c = merge(a.nxt, b.nxt)
            a.nxt = b
            b.nxt = c
            return a

        tail_a = self.get_tail_a()
        a, b = self.nxt, tail_a.nxt
        tail_a.nxt = None
        print(self.getlist(a))
        print(self.getlist(b))
        merge(a, b)



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
dhead.weave_recursive()
assert dhead.getlist(dhead.nxt) == list(range(1,11))




'''
weave back to back linked lists
135246
   s
      f    
first of all find where 2nd list is: O(n)
then cut it off, a and b: O(1)
then can do a'snext gets b, and b's next gets rec-call on a.next and b.next. 
'''
def find_second_head(head: ListNode) -> ListNode:
    fast = slow = head
    prevslow = None
    while fast:
        fast = fast.next.next
        prevslow = slow
        slow = slow.next
    return prevslow

def merge(head: ListNode) -> ListNode:
    def _merge(head: ListNode, otherhead: ListNode) -> ListNode:
        if not head:
            assert not otherhead
            return None
        

    prev = find_second_head(head)
    otherhead = prev.next
    prev.next = None
    otherhead.next = _merge(head.next, otherhead.next)
    head.next = otherhead
    return head
'''
weave back to back linked lists
135246
   s
      f    
first of all find where 2nd list is: O(n)
then cut it off, a and b: O(1)
then can do a'snext gets b, and b's next gets rec-call on a.next and b.next. 
'''
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, data, next: Optional[ListNode]=None) -> None:
        self.data = data
        self.next: Optional[ListNode] = None

    def __str__(self) -> str:
        curr = self
        res = []
        while curr:
            res += [curr.data]
            curr = curr.next
        return ''.join

def find_second_head(head: ListNode) -> Optional[ListNode]:
    fast = slow = head
    prevslow = None
    while fast:
        assert slow
        assert fast.next
        fast = fast.next.next
        prevslow = slow
        slow = slow.next
    return prevslow

'''
1 3
2 4

1->2->m(3,4)
3->4->N
'''
def merge(head: ListNode) -> Optional[ListNode]:
    def _merge(head: Optional[ListNode], otherhead: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            assert not otherhead
            return None

        assert otherhead
        otherhead.next = _merge(head.next, otherhead.next)
        head.next = otherhead
        return head
           
    prev = find_second_head(head)
    if not prev:
        return None
    assert prev
    prev.next = None
    otherhead = prev.next
    return _merge(head, otherhead)
 
otherhead = ListNode(2, ListNode(4, ListNode(6)))
head = ListNode(1, ListNode(3, ListNode(5,otherhead)))
print(head)
# reshead = merge(head)
# print(reshead)


'''
lessons learned: be careful, don't jump into structural code changes until you know
what you see the result mentally (or other) well
Given a linked list node, a1 such that
a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn, make a  linked list so that it becomes
a1 -> b1 -> a2 -> b2 -> ... -> an -> bn

a b c
r t x

a r ...
    b t ...
        c x 
            ...
can go recursive. how?  
return merge(a, b) # assume detached lists or put merged in a and return that
'''
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: str, next: Optional[ListNode]) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        curr = self
        res = []
        while curr:
            res += [curr.val]
            curr = curr.next
        return ''.join(res)

def partition(a: Optional[ListNode]) -> Optional[ListNode]:
    '''
    abcrtx
      ps
          f
    '''
    slowprev = None
    slow = fast = a
    while fast:
        assert slow
        assert fast.next
        fast = fast.next.next
        slowprev = slow
        slow = slow.next
    assert slowprev
    b = slowprev.next
    slowprev.next = None
    assert b
    return b

def merge_r(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    if not a:
        assert not b
        return None
    assert a and b
    b.next = merge_r(a.next, b.next)
    a.next = b
    return a

def merge_i(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    '''
    point at a, move a, move c, point at b, move b, 
      a
     qbd
     rtx
     cb

     c->a
    '''
    res = c = ListNode('', None)
    while a:
        assert b
        c.next = a
        a = a.next
        c = c.next

        c.next = b
        b = b.next
        c = c.next
    return res

def weave(a: Optional[ListNode], use_recursive: bool) -> Optional[ListNode]:
    b = partition(a)
    if use_recursive:
        return merge_r(a, b)
    return merge_i(a, b)

a = ListNode('a', ListNode('b', ListNode('c', ListNode('r', ListNode('t', ListNode('x', None))))))
print(a) # abcrtx -> arbtcx
print(weave(a, False))


'''
lessons learned: be careful, don't jump into structural code changes until you know
what you see the result mentally (or other) well
Given a linked list node, a1 such that
a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn, make a  linked list so that it becomes
a1 -> b1 -> a2 -> b2 -> ... -> an -> bn

a b c
r t x

a r ...
    b t ...
        c x 
            ...
can go recursive. how?  
return merge(a, b) # assume detached lists or put merged in a and return that
'''



from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: str, next: Optional[ListNode]) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        curr = self
        res = []
        while curr:
            res += [curr.val + ', ']
            curr = curr.next
        return ''.join(res)

def partition(a: Optional[ListNode]) -> Optional[ListNode]:
    '''
    abcrtx
      ps
          f
    '''
    slowprev = None
    slow = fast = a
    while fast:
        assert slow
        assert fast.next
        fast = fast.next.next
        slowprev = slow
        slow = slow.next
    assert slowprev
    b = slowprev.next
    slowprev.next = None
    assert b
    return b

def weave_recursive(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    if not a:
        assert not b
        return None
    assert a and b
    b.next = weave_recursive(a.next, b.next)
    a.next = b
    return a

def weave_iterative(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    '''
    point at a, move a, move c, point at b, move b, 
      a
     qbd
     rtx
     cb

     c->a
    '''
    res = c = a
    while a:
        assert b
        assert c
        a = a.next
        c.next = b
        c = b

        b = b.next
        c.next = a
        c = a
    return res

def weave_stacked(a: Optional[ListNode], use_recursive: bool) -> Optional[ListNode]:
    b = partition(a)
    if use_recursive:
        return weave_recursive(a, b)
    return weave_iterative(a, b)

a = ListNode('1', ListNode('2', ListNode('3', ListNode('4', ListNode('5', ListNode('6', None))))))
print(a)
print(weave_stacked(a, False))

a = ListNode('1', ListNode('2', ListNode('3', ListNode('4', ListNode('5', ListNode('6', None))))))
print(a)
print(weave_stacked(a, True))

'''
a b c n
  s
    f

a b n
s
f


a an
a   b  c d n
|  /
| / 
1   2  3 4 n
b


expected:       
a 1 b 2 c 3 d 4 n

a   b n 
| /
|/
1   2 n
t=an
'''
def find_mp(a):
  s=f=a
  while f.next and f.next.next:
    f=f.next.next
    s=s.next
  return s

def merge(a,b):
    if not a:
        assert not b
        return None
    a.next,temp=b,a.next
    b.next=merge(temp,b.next)
    return a

def weave_lists(a):
    p=find_mp(a)
    b=p.next
    p.next=None
    return merge(a,b)


class Node:
    def __init__(self,val,next=None) -> None:
       self.val=val
       self.next=next

b=Node('1',Node('2', Node('3')))
a=Node('a', Node('b', Node('c', None)))
# print(find_mp(a).val) # c
c=merge(a,b)
print(c.next.next.next.next.val) #c
print(c.next.next.next.next.next.val) # 3
#a b c 1 2 3
# a 1 b 2 c 3

b=Node('1',Node('2', Node('3')))
a=Node('a', Node('b', Node('c', b)))
weave_lists(a)
print(a.next.next.next.next.val) #c
print(a.next.next.next.next.next.val) # 3
