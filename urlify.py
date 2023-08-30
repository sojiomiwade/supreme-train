'''
replace each space with %20
there is enough space after replacements are done

approach 1: can use a new char array
time: O(n), space: O(n)
for each i, char in arr
    res.append(char)
    if char = ' '
        res[-1] = %
        res.append  2
        res.append 0
return res



'''
from typing import List
def urlify_linear_space(arr: List[str], truelen: int) -> List[str]:
    res = []
    for i in range(truelen):
        ch = arr[i]
        res.append(ch)
        if ch == ' ':
            res[-1] = '%'
            res.append(2)
            res.append(0)
    return res
urlify = urlify_linear_space

'''
approach 2: can do it in place
time: O(n), space: O(1)
given a string like
"Mr John Smith    ", 13
       ^
         ^
         ^
             ^   
"0123456789012
 

hand-wavy arg
space_count - get this from 0 to truelen - 1, count spaces,
  and bring it down as you go past from the back each space

right is calculated from left and space_count
start left from truelen to 0
    if arr[left] != ' '
        right = left + space_count * delta
        arr[right] = arr[left]
    else
        arr[right - 1] = 0
        arr[right - 2] = 2
        arr[right - 3] = %
        space_count -= 1
'''
def urlify_const_space(arr: List[str], truelen: int) -> List[str]:
    space_count = sum(
        1 if arr[i] == ' ' else 0 for i in range(truelen))
    right = 0
    for left in range(truelen - 1, -1, -1):
        if arr[left] != ' ':
            right = left + space_count * 2
            arr[right] = arr[left]
        else:
            arr[right - 1] = '0'
            arr[right - 2] = '2'
            arr[right - 3] = '%'
            space_count -= 1
    return arr
urlify = urlify_const_space

s, truelen = list("Mr John Smith    "), 13
print(urlify(s, truelen)) 

