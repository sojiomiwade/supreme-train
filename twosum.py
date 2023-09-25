'''
find in a given list, the indices, of two numbers such that their sum equals k

touch
------
go through and keep in hash table arr[i]: i
then when we also check arr[i], we just need to see if k - arr[i] is in hash table
and then we can return i, loc[k - arr[i]]

no sort
keep comp[x] as you go. 
and along the way, once you see comp[x], we are done
let comp[x] = idx of x
then we can return [idx[x], curr-idx]
time: O(n)
space: O(n)

sort: 
time: Omega(n lg n) 
space: O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for idx in range(len(nums)):
            if nums[idx] in comp:
                return [idx, comp[nums[idx]]]
            comp[target-nums[idx]] = idx


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orignums = nums[:]
        nums.sort()
        thesum = nums[0] + nums[-1]
        left, right = 0, len(nums) - 1
        while thesum != target:
            if thesum < target:
                left += 1
            else: 
                right -= 1
            thesum = nums[left] + nums[right]
        res = []
        for i in range(len(nums)):
            if orignums[i] in (nums[left], nums[right]):
                res.append(i)
        return res
'''
comp = {7: 0, }
retval = [1, 0]
'''
