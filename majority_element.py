'''
? 1 2 2 2 3 2 5
        ^
have,count=1,0
2 2 2 2 1 3 5
        ^
you look back (and count helps with this)
count=0 => in the past, all is balanced
count=x => there is a majority, m, and freq(m)-freq(not m)=x 
note that count is defined (as zero) before you start, since we have none
return cur
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if count==0:
                have=nums[i]
            if nums[i]==have:
                count+=1
            else:
                count-=1
        assert 'have' in locals()
        return have