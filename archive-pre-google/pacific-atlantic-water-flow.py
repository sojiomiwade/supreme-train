'''
on a DFS level, we have seeds for pacific from top and left
if something is already true do not DFS it. otherwise try to recursively
to try is to say it (all nbs) becomes true if it is bigger in height

at the end, the ans is all cells where preachable and areachable
3 2
1 6 5
0 1 4
can only visit it if water can flow down
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def visit(rp: int, cp: int, r: int, c: int, reachable) -> None:
            if not 0<=r<m or not 0<=c<n:
                return 
            if reachable[r][c]:
                return
            if rp is not None and heights[r][c]<heights[rp][cp]:
                return
            reachable[r][c]=True
            for dr,dc in ((-1,0),(1,0),(0,1),(0,-1)):
                visit(r,c,r+dr,c+dc,reachable)

        m,n=len(heights),len(heights[0])
        preachable=[[False for _ in range(n)] for _ in range(m)]
        areachable=[[False for _ in range(n)] for _ in range(m)]
        for r in range(m):
            visit(None,None,r,0,preachable)
            visit(None,None,r,n-1,areachable)
        for c in range(n):
            visit(None,None,0,c,preachable)
            visit(None,None,m-1,c,areachable)
        return [[r,c] for c in range(n) for r in range(m) if preachable[r][c] and areachable[r][c]]