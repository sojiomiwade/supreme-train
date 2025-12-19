'''
1 2 2 0 0 0
      t
7 5 6
cannot be done in constant space, 
can get a new array
merge the results, and dump it into nums1
    if top is bigger take bot and increment that
    otherwise increment top

2 3 | 0
  t
    b
1 |
topval,botval  3 i
nums1 [1 2 3]
              i
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        buf=nums1[:]
        top=bot=idx=0
        while top<m or bot<n:
            topval=botval=float('inf')
            if top<m:
                topval=buf[top]
            if bot<n:
                botval=nums2[bot]
            if topval<botval:
                nums1[idx]=topval
                top+=1
            else:
                nums1[idx]=botval
                bot+=1
            idx+=1