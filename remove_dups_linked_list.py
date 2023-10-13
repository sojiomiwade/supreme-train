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
from typing import Optional, List

        
class ListNode:
    def __init__(self, 
        val: Optional[int]=None, 
        next: Optional[ListNode]=None
        ) -> None:
        self.val = val
        self.next = next

    def delete_next(self) -> ListNode:
        delnode = self.next
        assert delnode
        self.next = delnode.next
        return delnode
        
class SLL:
    def __init__(self) -> None:
        self.tail = ListNode()
        self.head = ListNode()
        self.tail.next, self.head.next = self.head, self.tail
        
    def append_to_tail(self, val: int) -> ListNode:
        last = self.tail.next
        assert last
        last.next = ListNode(val)
        self.tail.next = last.next
        return last.next

    def as_list(self, node: ListNode) -> List[int]:
        res, curr = [], node
        while curr is not self.tail:
            assert curr
            res += [curr.val]
            curr = curr.next
        return res

    def remove_dups(self, node: Optional[ListNode]) -> None:
        have = set()
        curr = node
        while node is not dta:
            if node in have:
                self.delete_next(prev)
            node = node.next

ListNode()
# for x in range(1,10):
# todo remove the default spec of None for Node. it doesn't help much as there aren't a hundred places having Node(None, None)
# and it makes clear what you are passing