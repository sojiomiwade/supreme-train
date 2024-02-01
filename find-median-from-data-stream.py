'''
1 2 3 4 5 6 7 8 9
1 8 7 2 4 9 6 3 5 

maxheap=4 3 2 1
minheap=5 6 7 8 9         

h1 : 3 2 2 2 1
h2 : 5 6 7 8 9 

add(el) : 
if el is bigger than maxtop, insert into minheap. else insert into max.
if maxheap is bigger than minheap by 2, pop from maxheap into minheap
elif minheap is bigger than maxheap by 2, pop from minheap into maxheap

median : if len(maxheap)==len(minheap) : average of two tops
else : the top of the bigger one 
'''
class MedianFinder:

    def __init__(self):
        self.maxheap=[float('inf')]
        self.minheap=[float('inf')]

    def addNum(self, num: int) -> None:
        '''
        add 1 add 2 findMedian: -inf
        1>-inf
        maxheap : +inf
        minheap : 1 2 +inf
        num=5
        maxtop,mintop=3,6
        '''
        maxlen,minlen=len(self.maxheap),len(self.minheap)
        assert abs(maxlen-minlen)<2

        maxtop,mintop=-self.maxheap[0],self.minheap[0]
        if num>maxtop:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap,-num)
        
        maxlen,minlen=len(self.maxheap),len(self.minheap)
        if maxlen>minlen+1: # 1 2 --- x, 2 > 1
            x=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-x)
        elif minlen>maxlen+1:
            x=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-x)

    def findMedian(self) -> float:
        maxlen,minlen=len(self.maxheap),len(self.minheap)
        assert maxlen>1 or minlen>1
        maxtop,mintop=-self.maxheap[0],self.minheap[0]
        print(maxtop,mintop)
        if maxlen==minlen:
            return (maxtop+mintop)/2
        elif maxlen>minlen:
            return maxtop
        else:
            return mintop

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()