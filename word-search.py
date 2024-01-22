'''
DFS from every cell
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def exist(r: int, c: int, idx: int) -> bool:
            if idx==len(word):
                return True
            if (r,c) in visited:
                return False
            if not 0<=r<m or not 0<=c<n:
                return False
            if word[idx]!=board[r][c]:
                return False
            visited.add((r,c))
            doesexist=(
                exist(r+1,c,idx+1) or
                exist(r-1,c,idx+1) or
                exist(r,c+1,idx+1) or
                exist(r,c-1,idx+1))
            visited.remove((r,c))
            return doesexist

        m,n=len(board),len(board[0])
        for r in range(m):
            for c in range(n):
                visited=set()
                if exist(r,c,0):
                    return True
        return False