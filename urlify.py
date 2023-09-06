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
'''
urlify a string
john smith |<buffer>
john%20smith%20
input: name and true length
output: name urlified in place
stop: 12:20 - 
clarify: ascii only? 
example 
john smith |<buffer>
01234567890123456789
john%20smith%20
method 
sc = number of spaces to the left of right
right = truelen + 2 * sc - 1
j_
j%20
012345
right = 2 + 2*1 - 1 = 3
analysis: time: O(n) space: O(1)
' ' __> '%20'
 ^
right = 1 + 2 -1 = 2
'''
from typing import List
def urlify(s: List[str], truelen: int) -> List[str]:
    sc = sum(1 if s[i] == ' ' else 0 for i in range(truelen))
    right = truelen + 2 * sc - 1
    for i in range(truelen-1, -1, -1):
        if s[i] != ' ':
            s[right] = s[i]
            right -= 1
        else:
            s[right] = '0'
            s[right - 1] = '2'
            s[right - 2] = '%'
            right -= 3
    return s
lis = list('john smith     ')
print(urlify(lis, 11))
#john%20smith%20


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

