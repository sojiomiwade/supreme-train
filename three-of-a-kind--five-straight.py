'''
problem 1
if eveything is 3 or more of a kind, return True
3 1 3 1 1 3

problem 2
if we can collect 5 consecutive from the arr, 
and leave nothing in the arr, return True.
otherwise, return False

1 2 3 4 5  3 4 5 6 7  2 3 4 5 6

1 2 3 4 5 6 7
1 2 3 3 3 2 1
1 2 3 3 3 2 1
0 0 1 1 1 1 1

start from the lowest and try to get the whole thing to 0


'''
from typing import Counter, List
import collections


def kind3(arr: List[int]) -> bool:
    count=collections.Counter(arr)
    return all(x==3 for x in count.values())

# arr=[3, 1, 3, 1, 1, 3]
# print(kind3(arr))
# arr=[3, 1, 3, 1, 1, 3, 4]
# print(kind3(arr))


'''
1 2 3 4 5  3 4 5 6 7  2 3 4 5 6

1 2 3 4 5 6 7
1 2 3 3 3 2 1
1 2 3 3 3 2 1
0 0 1 1 1 1 1

1 2 3 4 5 3 4 5 6
1 2 3 4 5
1 1 2 2 2
1 1 2 2 2
0 0 1 1 1
start from the lowest and try to get the whole thing to 0
1 2 3 3 3 2 1
1 2 3 4 5 6 7 | n 7 | True
0 0 0 0 0 0 0
seeds [1 2 3 4 5 6 7]
       x
x,val 1,1


'''
def con5(arr: List[int]) -> bool:
    count=Counter(arr)
    seeds=sorted(count)
    n=len(count)
    for x in seeds:
        val=count[x]
        if val:
            for i in range(5):
                if x+i not in count or count[x+i]<val:
                    return False
                count[x+i]-=val
    return True

s='1 2 3 4 5 3 4 5 6'
arr=[int(x) for x in s.split()]
print(con5(arr))

s='1 2 3 4 5  3 4 5 6 7  2 3 4 5 6'
arr=[int(x) for x in s.split()]
print(con5(arr))
