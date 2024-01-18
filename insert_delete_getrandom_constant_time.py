class RandomizedSet:

    def __init__(self):
        self.ll,self.rll={},{}

    '''
    ll, rll
    insert: if not exists: add to ll, add reverse to rll
    remove: put last in 3's place in both lookup. 7 takes on 3's idx
    ie ll[7]=ll[3], del last in ll, del last in rll, rll[ll[7]]=7
    1 3 2 4 7
    0 1 2 3 4 <-- can do a random on these and reverse lookup back

      v     lv
    1 2 4 7
    0 2 3 1 <-- can do a random on these and reverse lookup back
            
    0 1 2 3 <-- can do a random on these and reverse lookup back
    1 7 2 4
    ^     ^
    '''
    def insert(self, val: int) -> bool:
        ll,rll=self.ll,self.rll
        if val in ll: return False
        ll[val]=len(ll)
        rll[len(rll)]=val
        return True

    def remove(self, val: int) -> bool:
        ll,rll=self.ll,self.rll
        if val not in ll: return False
        count=len(ll) #5
        lastval=rll[count-1] #7
        ll[lastval]=ll[val]
        rll[ll[lastval]]=lastval
        del ll[val]
        del rll[count-1]
        return True

    def getRandom(self) -> int:
        ll,rll=self.ll,self.rll
        count=len(ll)
        return rll[random.randrange(count)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()