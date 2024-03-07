'''
delete could just move the last element into the deleted slot
    must modify maps going both ways
random uses the rl to get element value
so insert is now a simple task
'''
class RandomizedSet:

    def __init__(self):
        self.vall,self.idxl={},{}

    def insert(self, val: int) -> bool:
        if val in self.idxl:
            return False
        count=len(self.vall)
        self.vall[count]=val
        self.idxl[val]=count
        return True

    '''
    2 8 4 5
    0 1 2 3
    2 8 4 5
    0 1 2 3
    idxl {51 --81--}
    vall {15 --35--}
    '''
    def remove(self, val: int) -> bool:
        if val not in self.idxl:
            return False
        idx=self.idxl[val]               # 1
        lastidx=len(self.vall)-1    # 3 
        lastval=self.vall[lastidx]       # 5
        self.idxl[lastval]=idx           #  
        self.vall[idx]=lastval

        # prune the lookups
        del self.vall[lastidx]
        del self.idxl[val]
        return True

    def getRandom(self) -> int:
        count=len(self.vall)
        idx=random.randrange(count)
        return self.vall[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()