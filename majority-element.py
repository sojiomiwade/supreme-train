'''
2 2
2/2 = 1

2 2 3 4 5
        c
ans=2
count=2

    count=
    seen
count starts at 0

3/2 = 1
c
repeat for each element
    if count is zero [no majority eleme]
        set ans to cur
    count += 1 if cur is ans else -1
return ans
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        ans=None
        for cur in nums:
            if not count:
                ans=cur
            count+=1 if cur==ans else -1
        return ans