'''
s = "jace"
t = "ecaj"
foo(s,t) -> true
method 1: find all permutations of s and see if t is there: O(n!)
method 2: dictionary counter
j: 1, a: 1, c: 1, e:1
time: O(n)
for each s-i, increment associated counter: O(n)
do same for t-i: O(n)
compare two counters, all keys should have same value: O(n)
total: O(n)
method 3: same as method 2, but hash table is arr[26] if a-z.
better than method 2, since hash table constant is avoided
'''
        
def isperm(s: str, t: str) -> bool:
    def count(s, counter) -> None:
        for ch in s:
            counter[ord(ch) - ord('a')] += 1

    scounter = [0] * 26
    tcounter = [0] * 26
    count(s, scounter)
    count(t, tcounter)
    return scounter == tcounter


def isperm_counter(s: str, t: str) -> bool:
    from collections import Counter
    scounter = Counter()
    tcounter = Counter()
    if len(s) != len(t):
        return False
    for sch, tch in zip(s, t):
        scounter[sch] += 1
        tcounter[tch] += 1
    return scounter == tcounter
isperm = isperm_counter

def isperm_sort(s: str, t:str) -> bool: 
    return sorted(s) == sorted(t)
isperm = isperm_sort

s, t, = "jace", "ecaj"
print(isperm(s, t)) # true
s, t, = "jace", "eecaj"
print(isperm(s, t)) # false
s, t, = "jacee", "eecaj"
print(isperm(s, t)) # true
s, t, = "jacee", "eecajk"
print(isperm(s, t)) # false
#null case? no
