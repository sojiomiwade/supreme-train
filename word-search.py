'''
DFS from every cell
T(n)=4*T(n-1) + 1
=4*(4*T(n-2)+1)+1
=4*(4*(4(T(n-3)+1))+1) + 1
=4**2
=4**n +   +4**3 ..4**2.4 + 1
=4**n + 4**n
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
        visited=set()
        for r in range(m):
            for c in range(n):
                if exist(r,c,0):
                    return True
        return False