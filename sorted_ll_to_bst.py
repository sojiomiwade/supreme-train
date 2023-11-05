'''
Hi James, nice to meet you! I would like to confess one omission (that I noticed shortly after the interview) that will show itself readily on execution: the right branching must ensure we don't fall off. We did this for the left branching. We can execute this for the right by adding a logic for both (and hence removing the left logic) allowing for a nice and elegant solution.  Renaming helper per your recommendation, we have: 
01234567890123456789012345678901234567890123456789012345678901234567890123456789

h->1<-t
'''

from __future__ import annotations
from typing import Optional, Tuple

class ListNode:
    def __init__(self, val:int, next: Optional[ListNode]) -> None:
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

#01234567890123456789012345678901234567890123456789012345678901234567890123456789
def get_tail(head: Optional[ListNode]) -> ListNode:
    prev = None
    while head:
        prev, head = head, head.next
    assert prev
    return prev

#01234567890123456789012345678901234567890123456789012345678901234567890123456789
def get_midprev(prevhead: ListNode, tail: ListNode) -> ListNode:
    slow = fast = prevhead.next
    prev = prevhead
    while fast is not tail:
        assert fast
        fast = fast.next
        if fast is tail:
            break
        assert fast
        fast = fast.next
        prev = slow
        assert slow
        slow = slow.next
    assert prev
    return prev

#01234567890123456789012345678901234567890123456789012345678901234567890123456789
'''
    t
    h
dh  1 
mp  m

(null, 1)

cbb(dh, 1)
    cbb(dh, dh) --> null
    cbb(1, 1) --> 
        1
       / \
'''
def _create_balanced_bst(
        headprev: ListNode, tail: ListNode) -> Optional[TreeNode]:
    if tail.next is headprev.next:
        return None

    midprev = get_midprev(headprev, tail)
    mid = midprev.next
    assert mid

    root = TreeNode(mid.val)
    root.left = _create_balanced_bst(headprev, midprev)
    root.right = _create_balanced_bst(mid, tail)
    
    return root

def create_balanced_bst(head: ListNode) -> Optional[TreeNode]: 
    tail = get_tail(head)
    dummyhead = ListNode(0, head)
    return _create_balanced_bst(dummyhead, tail)

head = ListNode(1, None)
print(create_balanced_bst(head))
