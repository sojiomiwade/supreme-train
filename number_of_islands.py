class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        run through grid and count number of 1s, 
        DFS at each 1 and set it to #
        '''
        def _numislands(r: int, c: int) -> None:
            if not 0<=r<m or not 0<=c<n or grid[r][c] != '1':
                return
            grid[r][c] = '#'
            _numislands(r+1, c)
            _numislands(r-1, c)
            _numislands(r, c+1)
            _numislands(r, c-1)

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    _numislands(i, j)
        return res