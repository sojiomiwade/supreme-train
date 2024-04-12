# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
heap el is [nodeval,listloc]
getmin each time, and put it into ans
use listloc from min to add to heap [if there's element in that list]
continue this until heap is empty
ans should be 1 -> 3 -> 7 -> n
0 | 1 7
1 | null
2 | 3
heap [  i10n i20n i00n]
minval,minloc 7007
node 3
val inf
ans [d -> 1 -> 3 -> 7]
                    cur
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans,INF=ListNode(),float('inf')
        heap=[(x.val,i,0,x) if x else (INF,i,0,None) for i,x in enumerate(lists)]
        heapq.heapify(heap)
        cur=ans
        while heap and heap[0][0]!=INF:
            minval,minloc,_,node=heapq.heappop(heap)
            cur.next=node
            cur=node
            val=node.next.val if node.next else INF
            heapq.heappush(heap,(val,minloc,0,node.next))
        return ans.next