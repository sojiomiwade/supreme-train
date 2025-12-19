'''
unsorted linked list: remove duplicates

1 1 1 --> 1

1 1 2 1 1 -> 1 2

2 3 4 5 1 -> 2 3 4 5 1
'''

from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, val, next: Optional[Node]) -> None:
        self.val = val
        self.next = next

def remove_dups(node: Optional[Node]) -> Optional[Node]:
    alreadyhave=set()
    cur = node
    while cur:
        alreadyhave.add(cur.val)
        while cur.next and cur.next.val in alreadyhave:
            cur.next = cur.next.next
        cur = cur.next
    return node

def printlist(node: Optional[Node]) -> None:
    cur = node
    while cur:
        print(f'{cur.val}', end=' ')
        cur = cur.next
    print()

tl1 = Node(1, Node(1, Node(1, None)))
tl2 = Node(1, Node(1, Node(2, Node(1, Node(1, None)))))
tl3 = Node(2, Node(5, Node(4, Node(4, Node(2, None)))))

printlist(tl1)
printlist(remove_dups(tl1))

printlist(tl2)
printlist(remove_dups(tl2))

printlist(tl3)
printlist(remove_dups(tl3))

