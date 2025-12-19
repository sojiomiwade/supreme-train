'''
implement a queue with a linked list
    need append to tail, and remove_from_head

    init with head and tail, so we don't have to 
    adjust these pointers
    h-> ... <-t
'''
from __future__ import annotations
from typing import Optional, Tuple

class Node:
    def __init__(self, key: int, data: str, next: Optional[Node]) -> None:
        self.key = key
        self.data = data
        self.next = next

class Queue:
    
    def __init__(self) -> None:
        self.head = Node(0,'',None)
        self.tail = Node(0,'',self.head)
        self.head.next = self.tail

    def peek(self) -> Optional[Tuple[int, str]]:
        if self.head.next is self.tail:
            return None
        res = self.head.next
        assert res
        return res.key, res.data

    '''
    h->a->b->c<-t

    '''
    def popfront(self) -> Tuple[int, str]:
        if self.peek():
            res = self.head.next
            assert res
            self.head.next = res.next
            return res.key, res.data
        raise IndexError('cannot pop from empty queue')

    '''
    h->a->b<->t
    h->a->b->c<->t
    '''
    def pushback(self, key: int, data: str) -> None:
        last = self.tail.next
        newnode = Node(key, data, self.tail)
        assert last
        last.next = newnode
        self.tail.next = newnode

    def isempty(self) -> bool:
        return self.head.next is self.tail

q = Queue()
print(q.peek()) #null

for x in range(5):
    q.pushback(x, '-'+str(x))

print(q.peek()) # 0

for x in range(5): # 01234
    print(q.popfront())

try:
    q.popfront()
except IndexError as ie:
    print('expected error, empty q', ie)
else:
    raise Exception('queue should be emtpy')