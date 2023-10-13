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
    def __init__(self, val: int, next: Optional[ListNode]) -> None:
        self.val = val
        self.next = next
        
class SLL:
    def __init__(self) -> None:
        self.head = ListNode(0, None)
        self.tail = ListNode(0, self.head)
        self.head.next = self.tail
        
    # h <-> t
    #    5
    # head next
    def append_to_tail(self, val: int) -> ListNode:
        last = self.tail.next
        assert last
        newnode = ListNode(val, None)
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

    def delete_next(self, prev: ListNode) -> ListNode:
        delnode = prev.next
        assert delnode and delnode is not self.tail
        prev.next = delnode.next
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
        '''
      N 2 2 N
      h c
        p n
        '''
        def find_prevnode(val: int, prevstart: ListNode) -> Optional[ListNode]:
            assert prevstart
            while prevstart.next is not self.tail:
                assert prevstart.next
                if prevstart.next.val == val:
                    return prevstart
                prevstart = prevstart.next
            return None

        curr = self.head.next
        prevstart = curr
        while curr is not self.tail:
            assert curr and prevstart
            prevstart = find_prevnode(curr.val, prevstart)
            if prevstart:
                self.delete_next(prevstart)
            else:
                curr = curr.next
                prevstart = curr

from itertools import chain
def make_list_with_dups() -> SLL:
    sll = SLL()
    for x in chain(range(5), range(5)):
        sll.append_to_tail(x+1)
    return sll

sll = make_list_with_dups()
assert len(sll.as_list()) == 2 * len(set(sll.as_list()))
sll.remove_dups2()
assert len(sll.as_list()) == len(set(sll.as_list()))

sll = make_list_with_dups()
assert len(sll.as_list()) == 2 * len(set(sll.as_list()))
sll.remove_dups()
assert len(sll.as_list()) == len(set(sll.as_list()))
