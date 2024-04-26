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

could put the references in a set for any one list, 
then iterate on the other until you find a node that is in the intersection

       c
          f
     d e 
b {d e f}
hA,hB (f null)
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        b=set()
        while headB:
            b.add(headB)
            headB=headB.next
        while headA:
            if headA in b:
                return headA
            headA=headA.next
        return None
