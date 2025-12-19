'''
arr1: 2 5 4 2 3 4, arr2 4 2
ans: 4 4 2 2 5 3
count:
idx 0 1 2 3 4 5 ...
cnt     2 1 2 1

loop through arr2, and put each element in ans, and decrment count
now loop through arr1, and for each occurfencd of that element in cout
put it in ans
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        