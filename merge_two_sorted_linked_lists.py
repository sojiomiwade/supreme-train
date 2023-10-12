# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
l2 1 2 3
l1 0     

'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        next = self.mergeTwoLists(list1.next, list2.next)
        list1.next = list2
        list2.next = next
        return list1# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 5 6
b
a
0 3 4

r = dh

l1 is always the smaller list
if 

 1
 1 2 4
 1 3 4
 c 2
dh
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dh = ListNode()
        while list1 or list2:
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')
            if val1 < val2:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return dh.next