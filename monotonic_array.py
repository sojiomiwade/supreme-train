'''
time 8:17 -- 8:29 = 12
1,3,3,  4,2,...
        ^
1 1 3 3 5
ne: 2
lt: can be 0 or 2 ...2 pass

3 3 1 1 0

ne times 2
lt times 0 pass, can also be 2 
if a not equal to b
    number of times a < b should equal number of times a != b or it should be 0
if can_check is set, only then do you check based on the first trigger
so as long as it is None, keep checking

count a <= b

corner: [1] => true. ok
3 3 
ne 0
lt 0

3 4 5
lt = 2
ne = 2

5 4 3
lt = 0
ne = 2
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        lt = ne = 0
        for i in range(1, len(nums)):
            lt += int(nums[i - 1] < nums[i])
            ne += int(nums[i - 1] != nums[i])
        return lt == 0 or lt == ne
        
