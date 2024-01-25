class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        '''
        DFS and count connected components
        '''
        def countship(r: int, c: int) -> None:
            if not 0<=r<m or not 0<=c<n or board[r][c]=='.' or (r,c) in visited:
                return
            visited.add((r,c))
            countship(r+1,c)
            countship(r-1,c)
            countship(r,c+1)
            countship(r,c-1)

        m,n=len(board),len(board[0])
        visited=set()
        count=0
        for r in range(m):
            for c in range(n):
                if board[r][c]=='X' and (r,c) not in visited:
                    countship(r,c)
                    count+=1
        return count

