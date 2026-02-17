# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4 3 2 1
#       s
#             f
# we should reverse from s.next down to the end and compare head down to s.prev
# 1 2 3 3 2 1
# s
# f

# 1 2
#   s
#     f

# t1 = s.prev
# h2 = s
# if f lands on nil
#     h2 = h2.next

# reverse(h2)
# h
# x<1<2 3 4
# p
#           c
#           t
# each iteration: temp goes to c.next; c.next becomes prev; prev goes to c; c goes to temp; 
# previous will be the head, tail is the passed in head

class Solution:
    def rev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, c = None, head
        while c:
            t = c.next
            c.next = p
            p, c = c, t
        return p

    def same(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> bool:
        while h1 and h2:
            if h1.val != h2.val:
                break
            h1, h2 = h1.next, h2.next
        return not h1 and not h2

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        s = f = head
        p = None
        while f and f.next:
            f = f.next.next
            p, s = s, s.next
        tail1 = p
        tail1.next = None
        head2 = s
        if f:
            head2 = head2.next
        head2 = self.rev(head2)
        return self.same(head, head2)
