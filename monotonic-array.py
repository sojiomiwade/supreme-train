'''
1 2 2 3
6 5 4 4 
1 2 2 3 6  5 4 4 
0 1 1 1 1 -1

if val is not set, 
    set val to curdiff
else (val is set)
    if curdiff is 0, pass 
    else: 
        if curdiff is not val, return false
        otherwise pass
1 3 2
    i
val,curdiff=2,-1
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        val=0
        for i in range(1,len(nums)):
            curdiff=nums[i]-nums[i-1]
            if not val:
                val=curdiff
            elif curdiff!=0 and curdiff*val<0:
                return False
        return Trueaggregate into two flags mono_inc and mono_dec; 1st checks we are always monotonically increasing, and similar for second. and just check that either flag is set


