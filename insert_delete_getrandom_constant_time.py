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

