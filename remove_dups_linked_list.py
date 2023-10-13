'''
write code to remove duplicates from an unsorted linked list
how could it be solved without a temp buffer

1 5 2 4 2 3 5
could implement an insertion sort or bubble sort, then remove neighboring duplicates: O(n**2), O(1)
could just use a hash table to remember what you've seen, and delete future such items. O(n), O(n)
without temp buffer...

then delete can also be seprate func
a b c
  ^

dh 1 2 3->4 dt
        ^
dt.next.next = newnode
dt.next = newnode
'''
from __future__ import annotations
from typing import Optional, List, Tuple

        
class ListNode:
    def __init__(self, 
        val: Optional[int]=None, 
        next: Optional[ListNode]=None
        ) -> None:
        self.val = val
        self.next = next
        
class SLL:
    def __init__(self) -> None:
        self.head = ListNode('head')
        self.tail = ListNode('tail')
        self.tail.next, self.head.next = self.head, self.tail
        
    # h <-> t
    #    5
    # head next
    def append_to_tail(self, val: int) -> ListNode:
        last = self.tail.next
        assert last
        newnode = ListNode(val)
        last.next = newnode
        newnode.next = self.tail
        self.tail.next = newnode
        return newnode

    def as_list(self) -> List[int]:
        res, curr = [], self.head.next
        while curr is not self.tail:
            assert curr
            res += [curr.val]
            curr = curr.next
        return res

    def delete_next(self, node: ListNode) -> ListNode:
        delnode = node.next
        assert delnode and delnode is not self.tail
        node.next = delnode.next
        return delnode

    # 5 1 2 3 4 5
    # d
    def remove_dups(self) -> None:
        have = set()
        prev = self.head
        curr = prev.next
        while curr is not self.tail:
            assert curr and prev
            if curr.val in have:
                self.delete_next(prev)
            else:
                prev = prev.next
            have |= {curr.val}
            curr = curr.next


    def remove_dups2(self) -> None:
        def find_node_by_val(val: int, prevstart: Optional[ListNode]) -> Optional[ListNode]:
            assert prevstart
            while prevstart.next is not self.tail:
                if prevstart.next == val:
                    return prevstart
                prevstart = prevstart.next
                assert prevstart
            return None

        prevstart = self.head
        start = curr = self.head.next
        while curr is not self.tail:
            assert curr and curr.val is not None
            prevstart = find_node_by_val(curr.val, prevstart)
            if prevstart:
                assert start
                self.delete_next(prevstart)
                found = startnode.next
            else:
                curr = curr.next

from itertools import chain
sll = SLL()
for x in chain(range(5), range(5)):
    sll.append_to_tail(x+1)
print(sll.as_list())
sll.remove_dups()
print(sll.as_list())

# todo remove the default spec of None for Node. it doesn't help much as there aren't a hundred places having Node(None, None)
# and it makes clear what you are passing