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

