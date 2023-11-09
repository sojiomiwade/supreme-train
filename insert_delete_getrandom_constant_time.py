''' 
insert(val): Inserts an item val to the set. If the value already exist, then don't insert it.
remove(val): Removes an item val from the set if present.
getRandom(): Returns a random element from current set of elements. Each element must have the same probability of being returned.
NOTE: average O(1) time for all three operations. 
a q r
0 1 2
array indexes allow for random
d[a] = 0
d[q] = 1
d[r] = 2
reflect[0] = a
reflect[1] = q
reflect[2] = r
could use same dict if keyspace was different, let's not assume this and use two dicts
insert (val)
    d[val] = count          val is unique
    reflect[count] = val    count is unique
    count ++
remove (val)
    val's count = d[val]
    do a "last" trick
        let's say 'a' got deleted
        reflect[val_idx] = reflect[count - 1]   # reflect[0] = reflect[3-1]
        d[reflect[count - 1]] = val_idx         # d[r] = 0
        del reflect[count]
        del d[val]
        count --
getRandom()
    rand_idx = rand(0, count)
    return reflect[rand_idx]
'''
d = {}
reflect = {}
count = 0
def insert(val: str) -> None:
    global count
    if val in d: 
        return
    d[val] = count
    reflect[count] = val
    count += 1

def remove(val: str) -> None:
    global count
    if val not in d:
        return
    val_idx = d[val]
    # let's say 'a' got deleted
    reflect[val_idx] = reflect[count - 1]   # reflect[0] = reflect[3-1]
    d[reflect[count - 1]] = val_idx         # d[r] = 0
    del reflect[count - 1]
    del d[val]
    count -= 1

from random import randrange
def getRandom() -> str:
    rand_idx = randrange(count)
    return reflect[rand_idx]

for i in range(10):
    insert(str(i))
for i in range(10):
    insert(str(i))
print(d.keys())
remove('3')
remove('5')
remove('5')
print(d.keys())
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())

# again
'''
insert(val): Inserts an item val to the set. If the value already exist, then don't insert it.
remove(val): Removes an item val from the set if present.
getRandom(): Returns a random element from current set of elements. Each element must have the same probability of being returned.
NOTE: average O(1) time for all three operations. 

use reflection of structure to getRandom
st[a] = 0, refl[0] = a
...
st[b] = 1, refl[1] = b
...
st[c] = 2, refl[2] = c

st[a] = 0, refl[0] = a
st[c] = 1, refl[1] = c

insert(val)
st[val] = count
refl[count] = val
count ++

getRandom:
return refl[rand(count)]

delete(val): #b, 4
st[refl[count-1]] =  count of element to delete = refl[val]
#st[z] = 4
refl[refl[val]] = refl[count-1]
#refl[4] = refl[25]  
st.pop
refl.pop
count --

time: 2:43 - 3:15 = 32
time: ^
space: overall: O(n),
'''
from random import randrange


class RandomSet:
    def __init__(self) -> None:
        self.st = {}
        self.refl = {}
        self.count = 0

    def insert(self, val) -> None:
        self.st[val] = self.count
        self.refl[self.count] = val
        self.count += 1

    def getRandom(self) -> str:
        return self.refl[randrange(self.count)]

    def delete(self, val): #b, 4
        delete_idx = self.st[val]
        last_el_val = self.refl[self.count-1]
        self.st[last_el_val] = delete_idx
        self.refl[delete_idx] = last_el_val
        self.st.popitem()
        self.refl.popitem()
        self.count -= 1

rs = RandomSet()
rs.insert('a')
rs.insert('c')
rs.insert('b')
print(rs.getRandom()) # a, b, or c
print(rs.getRandom()) # a, b, or c
rs.delete('c')
print(rs.getRandom()) # a, or b,
print(rs.getRandom()) # a, or b,

#again
'''
# /* 
# insert(val): Inserts an item val to the set. If the value already exist, then don't insert it.
# remove(val): Removes an item val from the set if present.
# getRandom(): Returns a random element from current set of elements. Each element must have the same probability of being returned.
# NOTE: average O(1) time for all three operations. 

#  */
time: 7:18 - 7:47 = 29 m
time comp: mandatory O(1)
space comp: 
key ob: insert can just be increment a count each time
getRandom. go to idx2val[idx], after getting a random idx
in range [0,count)
delete, say a
    lastidx = count - 1
    lastval = idx2val[lastidx]
    delidx = val2idx[val]
    delval = val
    val2idx[lastval] = val2idx[val] # d 0
    idx2val[delete] = lastval # 0, d
    del idx2val[a]
    del val2idx[lastidx]
    count --

a 0, 0 a
b 1, 1 b
d 2, 2 d
result:
d 0, 0, d
'''
from typing import Counter
from random import randrange


class RandomSet:
    def __init__(self) -> None:
        self.val2idx = {}
        self.idx2val = {}
        self.count = 0

    def insert(self, val) -> None:
        if val in self.val2idx:
            return
        self.val2idx[val] = self.count
        self.idx2val[self.count] = val
        self.count += 1

    def get_random(self) -> str:
        randidx = randrange(self.count)
        return self.idx2val[randidx]

    '''
    a 0, 0 a
    b 1, 1 b
    d 2, 2 d
    result:
    d 0, 0, d
    '''
    def delete(self, val) -> None:
        if val not in self.val2idx:
            return None
        lastidx = self.count - 1        # 2
        lastval = self.idx2val[lastidx] # d
        delidx = self.val2idx[val]      # 0
        self.val2idx[lastval] = delidx  # d 0
        self.idx2val[delidx] = lastval  #  0 d
        del self.val2idx[val]           # del a
        del self.idx2val[lastidx]       # del 2
        self.count -= 1        

rs = RandomSet()
for ch in 'abd':
    rs.insert(ch)
for _ in range(5):
    print(rs.get_random(),end=', ')
print()
rs.delete('a')
for _ in range(5):
    print(rs.get_random(),end=', ')
'''
lookup
4 7 2 3 8 9
0 1 2 3 4 5

rlookup
0 1 2 3 4 5
4 7 2 3 8 9

lookup
4 9 2 3 8
0 1 2 3 4

rlookup
0 1 2 3 4
4 9 2 3 8

insert: put in lookup[elem] = count, then incrment count

get-random: ret =rand(count). return rlookup[ret]

delete(delkey): 
adjust lookup
    delidx = lookup[delkey]
    lookup[rlookup[count-1]] = delidx
    #l[rl[5]] = 1: {9:1}
    del lookup[delkey] # bye bye 7

adjust rlookup
    rlookup[delidx] = rlookup[count-1] 
    #rl[]
    del rlookup[count-1]
'''
class RandomizedSet:

    def __init__(self):
        self.count = 0
        self.lookup = {}
        self.rlookup = {}

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        self.lookup[val] = self.count
        self.rlookup[self.count] = val
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        # adjust lookup
        if val not in self.lookup:
            return False
        delidx = self.lookup[val]
        self.lookup[self.rlookup[self.count-1]] = delidx
        del self.lookup[val] # bye bye 7

        # adjust rlookup
        self.rlookup[delidx] = self.rlookup[self.count-1] 
        del self.rlookup[self.count-1]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        return self.rlookup[random.randrange(self.count)]
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()'''
brute force: use a regular set, but get random will be linear
since we first gather all: O(n)
use a lookup and reverse lookup? 

1 3 5 7
0 1 2 3
0 1 2 3
1 3 5 7

1 3x 5 7
0 1x 2 31
   2    1

0 1  2 3x
1 37 5 7x
  1.   2
insert ^
delete(val):
    make the assiignmet first b4 deleting or you may not delete
    size: 4;  i,v: 1,3; li,lv: 3,7
'''
class RandomizedSet:
    def remove(self, val: int) -> bool:
        if val not in self.il:
            return False

        size = len(self.ril)
        idx = self.il[val]
        lidx, lval = size-1, self.ril[size-1]

        self.il[lval] = idx
        del self.il[val]

        self.ril[idx] = lval
        del self.ril[lidx]

        return True

    def __init__(self):
        self.il = {}
        self.ril = {}

    def insert(self, val: int) -> bool:
        if val in self.il:
            return False
        size = len(self.il)
        self.il[val] = size
        self.ril[size] = val
        return True

    def getRandom(self) -> int:
        return self.ril[random.randrange(len(self.il))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()