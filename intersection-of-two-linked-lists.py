# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    a b c
          \
            h i j k .
          /
q d e f g
reverse bot

-------------------- n
       ------------- m
       ------- -----
-------------- -----
    012345
            0123456 
0123456789
    ^
ans is 6
13
17
got it!
get the two list lengths m and n
get the diff m-n
now, advance diff on bigger list
and we are there



could put the references in a set for any one list, 
then iterate on the other until you find a node that is in the intersection

       c
          f
     d e 
b {d e f}
hA,hB (f null)
  1 2 
      6 7
  4 5
alen,blen 4 4
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        alen=blen=0
        a,b=headA,headB
        pa=pb=None
        while a:
            pa=a
            a=a.next
            alen+=1
        while b:
            pb=b
            b=b.next
            blen+=1
        if pa is not pb:
            return None
        if alen>blen:
            headA,headB=headB,headA
            alen,blen=blen,alen    
        b=headB
        for _ in range(blen-alen):
            b=b.next
        a=headA
        while a is not b:
            a,b=a.next,b.next
        return a