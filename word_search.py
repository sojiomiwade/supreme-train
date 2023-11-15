'''
A B C E
S F E S
A D E E
DFS each cell (can stop on finding)
keep a res. terminate when res is length of word (return true) or it is 
i-th char on DFS doesn't match i-th char of word
otherwise

no need for keeping a result. an idx is just fine


func e(r, c)
    
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def _exist(row: int, col: int, idx: int) -> bool:
            def valid() -> bool:
                res = 0 <= row < len(board)
                res = res and 0 <= col < len(board[0])
                res = res and (row,col) not in visit
                res = res and board[row][col] == word[idx]
                return res

            if idx == len(word):
                return True    
            if not valid():
                return False

            visit.add((row, col))
            res = _exist(row, col - 1, idx + 1)
            res = res or _exist(row - 1, col, idx + 1)
            res = res or _exist(row, col + 1, idx + 1)
            res = res or _exist(row + 1, col, idx + 1)
            visit.remove((row,col))
            return res

        res = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                visit = set()
                res = res or _exist(row, col, 0)
        return res
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def _exist(i, r, c):
            if i==m:
                return True
            if 0<=r<n1 and 0<=c<n2 and word[i]==board[r][c]:
                board[r][c],temp='#',board[r][c]
                up = _exist(i+1,r+1,c)
                do = _exist(i+1,r-1,c)
                ri = _exist(i+1,r,c+1)
                le = _exist(i+1,r,c-1)
                board[r][c] = temp
                return up or do or ri or le

        m,n1,n2 = len(word),len(board),len(board[0])
        for i in range(n1):
            for j in range(n2):
                if _exist(0,i,j):
                    return True
        return False'''
need visited
1 possible bruteforce: switch on w bits given mxn bits,
check for validity, and return true accordingly
complexity: 2**n
better is just recursively find the word checking *cell*
validity and word validity as you go, don't forget to not
revisit in any search (DFS)
complexity: m*n*(d**w)
BFS could be employed with a similar cost
pick DFS for simpler solution
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def _exist(r, c, wi):
            if wi==len(word):
                return True
            if 0<=r<m or 0<=c<n and (r,c) not in visited and word[wi]==board[r][c]:
                visited.add((r,c))
                exists=(
                    _exist(r+1,c,wi+1) or 
                    _exist(r-1,c,wi+1) or 
                    _exist(r,c+1,wi+1) or 
                    _exist(r,c-1,wi+1))
                visited.remove((r,c))
                return exists
            return False

        m,n=len(board),len(board[0])
        visited=set()
        for r in range(m):
            for c in range(n):
                if _exist(r,c,0):
                    return True
        return False