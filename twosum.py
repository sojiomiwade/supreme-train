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
'''
Merging 2 Packages
Given a package with a weight limit limit and an array arr of item weights, implement a function getIndicesOfItemWeights that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j. If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [4, 6, 10, 15, 16],  lim = 21

output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input] integer limit

[output] array.integer


2sum
4, 6, 10, 15, 16, lim = 21

put each number in a hashmap as we traverse array
check for complement for any given number. return true if it exists
time and space: n and n

could sort
4 6 10 15 16
l          r
move l or r depending on if sum less (move l) or greater (move r) than limit
when we find two, then go back to original array to find the respective indices
n lg n and  n(need sorted array + sort actually itself takes n)
'''
from typing import List


def get_indices_of_item_wights(arr: List[int], limit: int) -> List[int]:
    lookup = {}
    for idx, elem in enumerate(arr): # 
        if limit-elem in lookup: # 6 in lookup?
            return [idx, lookup[limit-elem]]
        lookup[elem] = idx # {4:0,6:1,}
    return []

arr = [4, 6, 10, 15, 16]
lim = 21
print(get_indices_of_item_wights(arr, lim)) # [3,1]