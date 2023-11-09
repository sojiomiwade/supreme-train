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
        return False