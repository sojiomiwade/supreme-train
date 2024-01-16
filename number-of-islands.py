'''
1 1
0 0
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def try2visit(r: int, c: int) -> None:
            if (r,c) in visited or not (0<=r<m and 0<=c<n) or grid[r][c]=='0':
                return
            visited.add((r,c))
            try2visit(r+1,c)
            try2visit(r-1,c)
            try2visit(r,c+1)
            try2visit(r,c-1)
        '''
        can go for DFS, on each of the mn cells, and count
        that cell if it hasn't been visited
        recursive call: try2visit on neighboring cells
        '''
        m,n=len(grid),len(grid[0])
        visited=set()
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    ans+=1
                    try2visit(i,j)
        return ans