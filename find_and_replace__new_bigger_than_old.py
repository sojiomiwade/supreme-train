'''
In a given string s, replace all spaces with %20
a b c
012345678
a%20b%20c
write from the back, otherwise you overwrite orig string
c gets shifted by two deltas
delta is replace key len - space key len = 2
b by one deltas
a by zero
back = n-1 + spacecount * delta # 2 * 2 = 4 + 4 = 8
for i in range(n-1, -1, -1):
  if s[i] != ' '
    s[back] = s[i]
    back -= 1
  else
    s[back], s[back-1], s[back-2] = '%20'
    back -= 3
return   

# corollary: what if we wanted to replace %20 by a space?
    v
a%20b%20c
012345678
a b c
a x 

   
%20%20  6-2*2 = 2
_
__
cannot write from the back, will delete b with c
can write from the front, since we won't be able to overwrite
right = left = 0
while right <= n
  if s[right:right+3] == '%20'
    s[left] = ' '
    right += 3
    left += 1
  else 
    s[left] = s[right]
    left += 1
    right += 1


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

'''
replace every occurence of a word f with amala
ab_f_bar
ab_amala_bar

ab_foo_ba_foo_r
   ^      |^ 
   amala
        |

abcfd
0123456789
abcamalad
    ^   |
r=7
start=3=7-5+1
3
first we can just write a new string, where every foo 
assume the input is a buffer array and do this inplace

if it werent' inplace, we can't just write, or we overwrite
so instead:
m=len(amala)
1) calculate length of new buffer: n+(m-1)*fcount
2) from the back replace each f with amala
'''
def replace(b, n, f, w):
    m=len(w) #5
    fc=sum(1 if c==f else 0 for c in b) #1
    nl=n+(m-1)*fc # 5+(4)=9
    right=nl-1 # =8
    left=n-1 #4
    for left in range(n-1,-1,-1):
        if b[left]!=f:
            b[right]=b[left]
            right-=1
        else:
            for i in range(m):
                b[right-m+1+i]=w[i] #7-4+0=3
            right-=m
    
b=list('abcfd    ')
b=list('abfcfd        ')
'''
01234567890
abcamalad
  l   
  r
'''
replace(b,6,'f','amala')
print(''.join(b)) #'abcamalad'