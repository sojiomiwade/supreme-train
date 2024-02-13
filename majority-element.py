'''
3 1 3 3 2
001 1
011 3
011 3
010 2
011 3

3 3 3 1 2
011
001
010
011

011
need a 32-size counter
then each val having count more than n/2 is your elem

-3
if the count[31]==1 then pad 1s to front
111111<<1

1010

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=[0 for _ in range(32)]
        for x in nums:
            mask=1
            for i in range(32):
                if x&mask!=0:
                    count[i]+=1
                mask<<=1
        ans=0
        mask=1
        n=len(nums)
        for i in range(32):
            if count[i]>n//2:
                ans|=mask
            mask<<=1
        return ans if count[31]<=n//2 else (-1<<32) | ans
