'''
exp  8 8 9 1 1 2 
get count of 8, then count of 9
then for sorting the rest. run through count and update arr1

arr2 8 9
arr1 9 2 8 1 8 1
arr1 8 8 9 1 1 2
count 0 2 1 0 0 0 0 0 0 0
idx  0 1 2 3 4 5
                 ^
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        MAX=1001
        count=[0]*MAX
        for el in arr1:
            count[el]+=1
        idx=0
        for el in arr2:
            arr1[idx:idx+count[el]]=count[el]*[el]
            idx+=count[el]
            count[el]=0
        for el in range(MAX):
            arr1[idx:idx+count[el]]=count[el]*[el]
            idx+=count[el]
        return arr1