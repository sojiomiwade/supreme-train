'''
arr1 3 2 1
arr2 1 2
count {11 21 31}
ans [1 2 3]
expected 1 2 3
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        count=Counter(arr1)
        arr2set=set(arr2)
        ans=[]
        for el in arr2:
            for _ in range(count[el]):
                ans.append(el)
        for el in arr1:
            if el not in arr2set:
                ans.append(el)
        return ans