'''
  2 2 1 1 1 2 2
          i
count 0
ans 2
- coming into a number, if count is 0, then pick cur as ans
- if ans is cur, then increment count, otherwise decrement count

3 2 3
    x
count 1
ans 3
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,ans=0,None
        for x in nums:
            if count==0:
                ans=x
            if x==ans:
                count+=1
            else:
                count-=1
        return ans
