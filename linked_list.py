'''
implement a linked list with append_to_tail
will add print_from_head to verify

order of input: 2 1 3 4
2->1->3->4
print: will match order of input from head

dh->2->1->x
       ^- tail

dh->4
    t


'''
from typing import Optional


class Node:
    def __init__(self, val: Optional[int]) -> None:
        self.val = val
        self.nxt: Optional[Node] = None

class LinkedList:
    def __init__(self) -> None:
        self.tail = self.head = Node(None)

    def append_to_tail(self, val):
        self.tail.nxt = Node(val)
        self.tail = self.tail.nxt

    def print(self) -> None:
        curr = self.head.nxt
        while curr:
            print(curr.val, end=', ')
            curr = curr.nxt
        print()

    '''
    h 2 1 3
      ^
    '''
    def delete_node(self, val: int) -> Optional[Node]:
        prev = self.head
        curr = prev.nxt
        while curr:
            if curr.val == val:
                prev.nxt = curr.nxt
                return curr
            prev = curr
            curr = curr.nxt
        return None

ll = LinkedList()
for num in [2,1,3,4]:
    ll.append_to_tail(num)
for x in (2,4,1,3):
    ll.delete_node(x)
    ll.print()
'''
134, 13, 3, .
'''
