'''
let us use a set. we don't care about equal 
1 2 2 2 2 3 4
all that matters is for the ne, it's always lt, or gt
so throw True in there if lt. otherwise throw false in there. 
at the end, the set length must be 1, (with element true)

0 means no less than found
1 2 2 -> ok
1 2 0

3 2 1
1 2 2 3

3 2 1 1
1 -1 0 vs 1 -1

0 no less than (mix of eq and/or gt) -> ok
1 all less than -> ok
2 both less and greater -> not ok
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        input_result = {nums[i-1] < nums[i] for i in range(1,len(nums)) if nums[i-1] != nums[i]}
        return len(input_result) < 2

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
        
'''
le
ge 
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        le=ge=0
        for i in range(1,len(nums)):
            if nums[i-1]<=nums[i]:
                le+=1
            if nums[i-1]>=nums[i]:
                ge+=1
        return (len(nums)-1) in (le,ge)