'''
shortest path from node k to all nodes, return the maximum
can use queue or BFS:
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
        #now use BFS
        #do not further process if a node cannot be made cheaper
        #if can be, make it cheaper, and then add the corresponding neighbors
        #if edges trigger adding other edges, complexity is E**2
        friend=defaultdict(dict)
        #{2:{0:1,1:2},3:{}}
        for u,v,w in times:
            friend[u][v]=w
        q=deque([(0,k)])
        ans=defaultdict(lambda :float('inf'))
        while q:
            cu,u=q.popleft()
            if cu<ans[u]:
                ans[u]=cu
                for v,cuv in friend[u].items():
                    q.append((cuv+cu,v))
        return max(ans.values()) if len(ans)==n else -1




        # ans=defaultdict(lambda :float('inf'))
        # q=deque([(0,k)])
        # friends,cost=defaultdict(list),{}
        # for (u,v,cuv) in times:
        #     friends[u].append((v,cuv))
        # while q:
        #     cx,nx=q.popleft()
        #     if cx<ans[nx]:
        #         ans[nx]=cx
        #         for ny,cxy in friends[nx]:
        #             q.append((cx+cxy,ny))
        # return max(ans.values()) if len(ans)==n else -1