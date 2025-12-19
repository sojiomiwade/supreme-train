'''
Given 2 strings write a method to decide if one is a permutation of the other

abcde
edcab
zeroth: sort both -> t,s: n lg n, n
first: hashmap counter increment the counter for a key if from s, decrement if from t. the counter must be all zeros for true. otherwise false.
'''
from collections import Counter


def checkperm(s: str, t: str) -> bool:
    assert None not in (s,t)
    if len(s)!=len(t):
        return False
    counter=Counter()
    for chs,cht in zip(s,t):
        counter[chs]+=1
        counter[cht]-=1
    return not any(counter.values())

s,t='abcde','edcab'
print(checkperm(s,t)) #true
s,t='abcde','edcab1'
print(checkperm(s,t)) #f
s,t='cde','edcab1'
print(checkperm(s,t)) #f
s,t='111','111'
print(checkperm(s,t)) #t
s,t=None,None
print(checkperm(s,t)) #exception

