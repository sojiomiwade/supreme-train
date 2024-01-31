from collections import Counter
from typing import List

# if eveything is 3 or more of a kind, return True
def kind3(arr: List[int]) -> bool:
    '''
    2 3 3 3 3 
    '''
    count=Counter(arr)
    return all(xcount>2 for (x,xcount) in count.items())

a='23333'
arr=[int(x) for x in a]
print(kind3(arr)) # False

a='2223333'
arr=[int(x) for x in a]
print(kind3(arr)) # True

# if we can collect 5 consecutive from the arr, 
# and leave nothing in the arr, return True.
# otherwise, return False
'''
1 2 3 3 4 4 5 5 6 7
1 1 2 2 2 2 2 2 1 1  
0 0 1 1 1 1 1 1 1 1
    0 0 0 0 0 0 1 1
              
'''
def is_straight(arr: List[int]) -> bool:
    arr=sorted(arr)
    count=Counter(arr)
    for x in arr:
        if count[x]:
            for idx in range(5):
                count[x+idx]-=1
    return not any(count.values())


arr=[1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8]
print(is_straight(arr)) # True

arr=[1, 2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 8]
print(is_straight(arr)) # False