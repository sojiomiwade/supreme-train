'''
could use a set, and if we ever see something we've seen, 
    then return true
    at the end return false. 
    time,space=O(n),O(n) <--may not read all elements (in time and space)

101
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=set()
        for x in nums:
            if x in count:
                return True
            count.add(x)
        return Falsecan also use sorting
