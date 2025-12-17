'''
there is a visited we need to backtrack out of
time O(mn * 4**(mn))
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def exist(r: int, c: int, idx: int):
            if idx==W:
                return True
            if (r,c) in visited or not(0<=r<m and 0<=c<n) or word[idx]!=board[r][c]:
                return False
            visited.add((r,c))
            ans=False
            idx+=1
            if exist(r-1,c,idx) or exist(r+1,c,idx) or exist(r,c-1,idx) or exist(r,c+1,idx):
                return True
            visited.remove((r,c))
            return False

        visited=set()
        m,n=len(board),len(board[0])
        W=len(word)
        for r in range(m):
            for c in range(n):
                assert not visited
                if exist(r,c,0):
                    return True
        return False