'''
'''
from typing import List


def threesum(arr: List[int]) -> bool:
    for i,x in enumerate(arr):
        compslookup={}
        for j in range(len(arr)):
            diff=-x-arr[j]
            if j!=i and (diff in compslookup) and (compslookup[diff] not in (i,j)):
                return True
            compslookup[arr[j]]=j
    return False

arr=[-6,3,3,]
print(threesum(arr)) # true
arr=[3,-6]
print(threesum(arr)) # false
