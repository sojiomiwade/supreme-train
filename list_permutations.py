'''
Provide a list of all permutations of a string, excluding duplicates

abcd
32  ^
current function loops over all possibilities for this idx
time: n * n * ... * n = n**m
hmmm. can there be duplicate chars if soo 
aa -> aa and aa? 


'''
from typing import List


def listperms(s: str) -> List[str]:
    def listperms(idx: int) -> None:
        buf.append(s[idx])
        have.add(idx)
        if len(buf)==n:
            ans.append(''.join(buf))

        for i in range(n):
            if i not in have:
                listperms(i)

        buf.pop()
        have.remove(idx)

    if not s:
        return []
    n,have,buf=len(s),set(),[]
    ans=[]
    for i in range(n):
        listperms(i)
    return ans

from math import factorial
#buf : [a,]
#have : {a}
s='abcd'
lps=listperms(s)
print(lps)
assert len(lps)==factorial(len(s))
# abc acb bac bca cab cba -> 6

s='abcde'
lps=listperms(s)
print(lps)
assert len(lps)==factorial(len(s))
