'''
2 2 2 2 1 3 5
        ^
153

zy5x5    <--we make 00101 since {x,y,z}<5 
approach: get the max freq, and make a number having only those bit freq equal to maxfreq

when -ve, we have
11111| 1|5xyzz5
      32
   0000000000|1|100001      <---wrong cuz it's positive
 | 1111111111|1|000000
   1111111111|
111110
000010
1111
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=0
        mask=1
        n=len(nums)
        for i in range(32):
            freq=0
            for x in nums:
                freq+=bool(mask&x)
            if freq>n//2:
                res|=mask
            mask<<=1
        if (1<<31)&res != 0: #bit 31 is set => number is negative
            res|=-1<<31
        return res