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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
can try to enumerate all possible BST at ~2**n
better to see if sorted list can help

1 2 3 4 5 6
ht=1,5
                    3 123456
        1 12                           5 456
 1n-null     22 2                44 4       66 6
           2n    n2            4n.   n4

get the median and make it root
set left to l2b(head,prev)
set right to l2b(next,tail)
return root

find-median: 
1
s
f
return prev because we need it, can derive median then

1
f
s
                123 (2)
             11            33
             
p=null
m=1
mn=null

 1234
ps
 f
ht=11
p=1
m=2
mn=2
             2
           /   \
          1     3
                 \
                   4
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def l2b(h,t):
            if not h or not t:
                return None
            p=mp(h,t)
            mid=h
            if p: mid=p.next
            midnext=mid.next
            if mid is t: midnext=None
            root=TreeNode(mid.val)
            root.left=l2b(h,p)
            root.right=l2b(midnext,t)
            return root

        '''
         1234
         ps
            f
        '''
        def mp(h,t): #14
            f=s=h
            p=None
            while f is not t:
                f=f.next
                if f is t:
                    break
                f=f.next
                p=s
                s=s.next
            return p

        cur=head
        prev=None
        while cur:
            prev,cur=cur,cur.next
        return l2b(head, prev)
