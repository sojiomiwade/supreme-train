'''
0123
1221
  i
idx,num : 31
first : 10 21
count : 12 22
deg,res: 2,2
3-0+1
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first,count={},Counter()
        deg=res=0
        for idx,num in enumerate(nums):
            first.setdefault(num,idx)
            count[num]+=1
            if count[num]>deg:
                deg=count[num]
                res=idx-first[num]+1
            elif count[num]==deg:
                res=min(res,idx-first[num]+1)
        return res