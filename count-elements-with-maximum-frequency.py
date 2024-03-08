'''
get the maximum frequency. then iterate through the array counting elements having that frequency
1 pass over nums to get max
another pass over count to get result
1 1 3 2 2
count {12 31 22}
maxf 4
return  
'''
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxf=max(count.values())
        return sum(maxf for num,freq in count.items() if freq==maxf)