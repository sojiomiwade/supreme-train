'''
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
print(dd(s, t)) # 9
