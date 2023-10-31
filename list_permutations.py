'''
Provide a list of all permutations of a string, excluding duplicates
time should be O(n!)
space should be O(n) excluding the resultant list
example
input: abc
output: abc, acb, bac, bca, cab, cba 
my approach
in exponential time, we can enumerate all, but we need a way to make 
func list_perms(s: string) -> List[string]
    res = ''
    mainres = []
    permute(s, res, mainres)
    return mainres

func permute(s: string, res: string, mainres)
    if s.empty or res == len(s):
        mainres += res
        return
    for each char ch in s
        res += ch
        remove ch from s  <--
        permute(s, res, mainres)
        res -= ch
        add ch back to s
    
it factorial; can do this with a DLL or with a ?set?
explore set
abcde
so not with set, but dictionary of index:isused, 
nope won't work in the time we want either, since we must still
loop over all s per recursion call
so we are left with DLL

node remove:
h-a-b-c-d-e-t
  ^
h-a-b-c-d-e-t
p ^
'''
from typing import List, Optional

class Node: 
    def __init__(self, val, prev) -> None:
        self.val = val
        self.prev = prev
        self.nxt: Optional[Node] = None

class DLL:
    def __init__(self, s) -> None:
        self.head = Node(None, None)
        self.tail = Node(None, self.head)
        prev = self.head
        for i in range(len(s)):
            curr = Node(i, prev)
            prev.nxt = curr
            prev = curr
        self.tail.prev = prev
        prev.nxt = self.tail

    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def addback(self, node):
        temp = node.prev.nxt
        node.prev.nxt = node
        temp.prev = node

def list_perms(s: str) -> List[str]:
    def permute() -> None:
        if len(res) == len(s):
            mainres.append(''.join(s[i] for i in res))
            return
        curr = sDLL.head.nxt
        while curr != sDLL.tail:
            assert curr is not None
            res.append(curr.val)
            sDLL.remove(curr)
            permute()
            res.pop()
            sDLL.addback(curr)
            curr = curr.nxt

    res = []
    mainres = []
    sDLL = DLL(s)
    permute()
    return mainres

print(list_perms('abc')) # [abc, acb, bac, bca, cab, cba]


#again
'''
list all permutations of a string s
a bc
acb
bac
bca
cab
cba
alg: recursively, remove one char from all in string given you, add that to result (prefix), and pass the new string on, along with the result for concatenation 
abc
'''
from typing import List


def permute(s: str) -> None:
    perm(s, [], 0)

def perm(rem: str, prefix: List[str], prefix_len) -> None:
    if prefix_len == len(s):
        print(''.join(prefix))
        return
    for i in range(len(rem)): # a
        prefix.append(rem[i])
        perm(rem[:i] + rem[i+1:], prefix, prefix_len+1)
        prefix.pop()

s = 'a'
permute(s) # abc, acb, bac, ...
s = 'abc'
permute(s) # abc, acb, bac, ...




'''
Provide a list of all permutations of a string

example
input: abc
output: abc, acb, bac, bca, cab, cba 

to get the string of length k 
for every string length k-1, t, for every char in s not in t
resk = place k in every position in between. 

left={d,c},  
 a b c
^ ^ ^ ^

tabulate the res[k]
with res[1] is length of s, and each t there is equal each character of s

we can do above until k == n

s = ab
expres = ab ba
tab = [[a, b], [] ]

 a b c
^ ^ ^ ^

ba, ab
1st: '' + ch + all. 
last: all + ch + 
'''
from typing import List


def all_perms(s: str) -> List[str]:
    n = len(s)
    tab = [[]]
    for ch in s:
        tab[0].append(ch)
    for k in range(1, n): # 1 time => correct
        tab.append([])
        for t in tab[k-1]: #take a k-1 string
            #all the characters not in t
            candset = set(s) - set(t)
            for ch in candset:
                for i in range(1 + len(t)):
                    tab[-1].append(t[:i] + ch + t[i:])
    print(tab)
    return tab[-1]

s = 'abc'
print(all_perms(s))


'''
Provide a list of all permutations of a string

example
input: abc
output: abc, acb, bac, bca, cab, cba 

to get the string of length k 
for every string length k-1, t, for every char in s not in t
resk = place k in every position in between. 

left={d,c},  
 a b c
^ ^ ^ ^

tabulate the res[k]
with res[1] is length of s, and each t there is equal each character of s

we can do above until k == n

s = ab
expres = ab ba
tab = [[a, b], [] ]

 a b c
^ ^ ^ ^

ba, ab
1st: '' + ch + all. 
last: all + ch + 
'''
from typing import List

# 
def all_perms(s: str) -> List[str]:
    n = len(s)
    tab = [[]]
    for ch in s:
        tab[0].append(ch)
    for k in range(1, n): # 1 time => correct
        tab.append([])
        for t in tab[k-1]: #take a k-1 string
            #all the characters not in t
            candset = set(s) - set(t)
            for ch in candset:
                    tab[-1].append(ch + t[:])
        tab[k-1] = []
    return tab[-1]

s = 'abcdef'
print(len(all_perms(s)))


'''
Provide a list of all permutations of a string

example
input: abc
output: abc, acb, bac, bca, cab, cba 

first char is base case
abc = 
 a b
^ ^ ^ <-- put c in all those positions
repeat for each result (just ba in this case)

return 
'''
from typing import List

#complexity: T(n) = n * n * T(n-1)
'''
n

k = n**2
n=4
4**2 * T(3)
       3**2 * T(2)
              2**2 * T(1)
                      1
(n**2)! <--- result
k * 
 k-1 k-2 k-3
3 2 1
'''
def allperms(s: str) -> int:
    def helper(n: int) -> List[str]: #abc, 2
        if n == 1:
            return [s[0]]
        res = []
        for t in helper(n-1): 
            for i in range(n): #3
                res.append(t[:i] + s[n-1] + t[i:])
        return res
    if not s:
        raise ValueError('input is null or empty')
    return len(helper(len(s))) # abc

s = 'abcde'
print(allperms(s))'''
list all permutations of length n
abcde
pre = 'bc'
rem = 
 a d e
    ^
|abcde
 ^
a|cde

put prefix everywhere in remaining
how to generate prefix? by s

abcde
^

        bcde,a
    cde,ab      bde,ac

acde,b
abde,c

abc
  ^
bc,a
    c,ab
        abc
    b,ac
        acb
ac,b
    c,ba
        cab
    a,bc
        bca
ab,c
'''
from typing import List



def allperms(s: str) -> List[str]:
    def _allperms(rem: str, prefix: str) -> None:
        if len(prefix) == len(s):
            res.append(prefix)
        for i in range(len(rem)):
            _allperms(rem[:i] + rem[i+1:], prefix + rem[i])

    res = []
    _allperms(s, '')
    return res

s = 'abcde'
res = allperms(s)
print(res, len(res))
