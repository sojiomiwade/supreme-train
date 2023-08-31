'''
Given 2 strings write a method to decide if one is a permutation of the other
carb
barc
for each char, get it's frequency into a hash map
can use the same hash table, one string increments the counter of ch, the other decrements it. at the end, if the map has all zeros in it, then true; else false
time: O(n), space: O(n) for one counter map

alternatively, sort both strings. and return true if they're equal
time: O(n lg n), space: O(1)
'''
from collections import Counter
def is_perm_equal(s: str, t: str) -> bool:
    counter = Counter()

    for sch, tch in zip(s, t):
        counter[sch] += 1
        counter[tch] -= 1
        if counter[sch] == 0:
            del counter[sch]
        if counter[tch] == 0:
            del counter[tch]
    return len(s) == len(t) and len(counter) == 0

s, t = 'barc', 'carb'
print(is_perm_equal(s, t)) # true
s, t = 'barc', 'carbb'
print(is_perm_equal(s, t)) # false
s, t = 'barcb', 'carbb'
print(is_perm_equal(s, t)) # true
s, t = '', ''
print(is_perm_equal(s, t)) # true
s, t = 'B', ''
print(is_perm_equal(s, t)) # false
