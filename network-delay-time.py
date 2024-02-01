'''


shortest path from node k to all nodes, return the maximum
can use BFS (queue) or heap:
queue starts with (0,2)
11 13 
{2:0 1:1}

(9,4) -- 4 got added by say 2
but later (2,4) gets added by 3, and damages are fixed
cost: 
14 .5 .5
10 1 1 1 1 
cost is just all the edges considered: O(V + E lg E)
spath[k]=

(2,3) (4,x)
   -  3 - - - 
 /
1-x----------2
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        heap:
        heap need not be exhausted? if so, then can use the len(ans)?
        no cause we will never reach e, so let's exhaust heap. just 
        deny something popped if it's too big.
        time,space: O(E lg E), O(E)
                a --- b
                |  9  |     e
                c --- d
        '''
        arr=[(0,k)]
        f=defaultdict(dict)
        ans=defaultdict(lambda :float('inf'))
        for u,v,w in times:
            f[u][v]=w
        while arr:
            cu,u=heapq.heappop(arr)
            if u in ans:
                assert ans[u]<=cu
            else:
                ans[u]=cu
                for v,cuv in f[u].items():
                    heapq.heappush(arr,(cuv+cu,v))
        return -1 if len(ans)!=n else max(ans.values())
