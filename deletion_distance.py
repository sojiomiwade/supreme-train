'''
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3
d  og
fr og

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0

Constraints:
[input] string str1
[input] string str2
[output] integer
define d_ij as del(s[:i], t[:j])
=> ans is d_mn
consider all possibilities
if a char will cause a del, remove it imm
otherwise, take the minimum of del on either s[1:],t and then s,t[1:]; add 1 ==> memo ==> d[1][0] ==> ans is d[0][0]
base case: if s or t is empty, return the len of the other.
run time expo. can memoize? yes
d_ij = del(s, t, i, j), i and j are "lengths"

so size of d is m+1,n+1

del(s, t) = del(s[:], 

time: 8:10 - 8:47 = 37 m
e l b o w i t
2 3 2 3         

       i
h e a t
h i t
j
-------
h t
h t

'''

def deldist(s: str, t: str) -> int:
    def helper(i: int, j: int) -> int: # 1 1
        if d[i][j] != -1:
            return d[i][j]
        if i == m or j == n: # 4, 5
            d[i][j] = max(m - i, n - j)
            return d[i][j]
        if s[i] == t[j]:
            d[i][j] = helper(i + 1, j + 1)
            return d[i][j]
        remove_in_s = helper(i + 1, j)
        remove_in_t = helper(i, j + 1)
        d[i][j] = 1 + min(remove_in_s, remove_in_t)
        return d[i][j]
    
    m, n = len(s), len(t)
    d = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return helper(0, 0) # ans distance from s0 and t0 to their ends
    
s, t = 'b', 'a' # 2
print(deldist(s, t)) # 

s, t = 'a', 'a' # 0
print(deldist(s, t)) # 

s, t = 'hit', 'heat' # 3
print(deldist(s, t))



Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

heat
hit


By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer

func dd(s, t): int
    if s[-1] == t[-1]
        return dd(s[:-1],t[:-1])
    if s or t equals ''
        return max(len(s), len(t))
    return 1 + min( dd(s[:-1], t), dd(s, t[:-1]))
'''

def dd(s: str, t: str) -> int:
    m, n = len(s), len(t)
    memo = [[-1 for c in range(n)] for r in range(m)]
    def dd_helper(send_loc: int, tend_loc: int) -> int:
        if min(send_loc, tend_loc) == -1:
            return 1 + max(send_loc, tend_loc)
        if memo[send_loc][tend_loc] != -1:
            return memo[send_loc][tend_loc]

        if s[send_loc] == t[tend_loc]:
            res = dd_helper(send_loc - 1, tend_loc -1)
        else:
            res = 1 + min(
            dd_helper(send_loc -1, tend_loc), 
            dd_helper(send_loc, tend_loc -1))
        memo[send_loc][tend_loc] = res
        return res

    return dd_helper(len(s) - 1, len(t) - 1)

s, t = 'ab', 'qcb'
print(dd(s, t)) # 3
s, t = 'some', 'thing'


#tabulation
def deletion_distance(str1, str2):
  m, n = len(str1), len(str2)
  d = [[0 for j in range(n+1)] for i in range(m+1)]
  for j in range(n+1):
    d[0][j] = j
  for i in range(m+1):
    d[i][0] = i
  for i in range(1,m+1):
    for j in range(1,n+1):
      if str1[i-1] == str2[j-1]:
        d[i][j] = d[i-1][j-1]
      else:
        d[i][j] = 1 + min(d[i-1][j], d[i][j-1])
  return d[m][n]

s, t = "heat", "hit"
print(deletion_distance(s,t))
print(dd(s, t)) # 9

#--deletion distance again, 
'''
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0
    
input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0 
    
Constraints:
[input] string str1
[input] string str2
[output] integer
        
0123        
 d og
 fr og   
0123        
t(1,2) = 
(d, fr) = (,fr) or (d, r) + 1 = 2
(brg, frog) = (r,frog) or (
t(1,1:n) = 1,
t(2,) = 
t(3,)

abc
cab

ab, ab

(ab,ba) = (a,ba) (ab, b)

tab(i,j) = dd(si, tj), i in [0,m], j in [0,n]
=>dim(d) = (m+1,n+1)
=> tab(0,j) = j and tab(i,0) = i
ex: tab(0,2) = dd('',fr) = 2
tab(i,j) = ?
    tab(i-1,j-1) if si[-1]=tj[-1]   #....x and ..x
    1+min(tab(i,j-1), min(i-1,j)    if si[-1]!=tj[-1]
dog
tab[4][5]

'''
'''
0123
     
 dog
 frog
 
tab[0] = j 
tab[1] = init just the 1st element to nothing, we will do this in loop

loop in a way to set one row based on the previous row set
    do this with modulo: use i%2

for i in [:m]
    tab[i%2] # setting 
0 01234
1  
2

'''
def deletion_distance(s: str, t: str) -> int:
    m, n = len(s)+1, len(t)+1
    tab = [[0 for _ in range(n)] for _ in range(2)]
    for j in range(1,n):
        tab[0][j] = j
    for i in range(1,m):
        tab[i%2][0] = i
        for j in range(1,n):
            if s[i-1] == t[j-1]:
                tab[i%2][j] = tab[(i+1)%2][j-1]
            else:
                tab[i%2][j] = 1+min(tab[i%2][j-1],tab[(i+1)%2][j])
    return tab[(m-1)%2][n-1] #'ab'->m=3
s, t = 'dog', 'frog'
print(deletion_distance(s,t)) # 3 -> og
s, t = 'ba', 'ab'
print(deletion_distance(s,t)) # 2 -> a or b
s, t = 'ba', ''
print(deletion_distance(s,t)) # 2 -> ''
s, t = 'ba', 'ba'
print(deletion_distance(s,t)) # 0 -> 'ba'
s, t = '', ''
print(deletion_distance(s,t)) # 0 -> ''

