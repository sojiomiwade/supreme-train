'''
if we can put the half larget and smallest in two heaps, then 
median is (i) the heap with the more elements or (ii) the average of 
two heaps. 
should be minheap for large and maxheap for small
can just maybe keep the small one the bigger always!
    => if large and small size differ, then pick from small. otherwise do the average
4 8 1 0 3 2 5 7
small 3 2 1 0
large 4 5 7 8

if el is bigger than stop, put it in large. otherwise put it in small
rebalance the heaps

2 3 1
small  -2 -1 INF
large  3 INF

1 2 3
small -1 INF
large  2 3 INF
'''
class MedianFinder:
    INF=float('inf')
    def __init__(self):
        self.small,self.large=[self.INF],[self.INF]

    def addNum(self, num: int) -> None:
        if num>-self.small[0]:
            heapq.heappush(self.large,num)
            if len(self.large)==2+len(self.small):
                heapq.heappush(self.small,-heapq.heappop(self.large))
        else:
            heapq.heappush(self.small,-num)
            if len(self.small)==2+len(self.large):
                heapq.heappush(self.large,-heapq.heappop(self.small))

    def findMedian(self) -> float:
        # print(self.small,self.large)
        if len(self.large)==len(self.small):
            sval=-self.small[0]
            lval=self.large[0]
            return (sval+lval)/2
        if len(self.large)>len(self.small):
            return self.large[0]
        return -self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()