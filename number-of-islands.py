'''
from driver visit all cells: if any cell is unvisited and it is a '1'
    increment a count, and DFS there to visit the corresponding component
return count
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def comp_visit(r:int, c:int) -> None:
            if 0<=r<m and 0<=c<n and (r,c) not in visited and grid[r][c]=='1':
                visited.add((r,c))
                comp_visit(r+1,c)
                comp_visit(r-1,c)
                comp_visit(r,c+1)
                comp_visit(r,c-1)

        m,n=len(grid),len(grid[0])
        count=0
        visited=set()
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1' and (r,c) not in visited:
                    count+=1
                    comp_visit(r,c)
        return count