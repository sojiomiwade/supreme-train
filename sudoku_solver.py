'''
basic idea, set a cell only to a valid value
valid means the sub doesn't have it, and the row and col don't have it

opts={(0,2):12345679,(0,4):...,}

for any cell, for each valid opt
  put that there (backtracking),
  if we can fill the board the answer is true. otherwise false
  
'''
def sudoku_solve(board):
  def rowlacks(r,v):
    for c in range(9):
      if board[r][c]==v:
        return False
    return True
  
  def collacks(c,v):
    for r in range(9):
      if board[r][c]==v:
        return False
    return True

  def sublacks(r,c,v):
    sc=(c//3)*3
    sr=(r//3)*3
    for i in range(3):
      for j in range(3):
        if board[sr+i][sc+j]==v:
          return False
    return True
  
  def _ss():
    for r in range(9):
      for c in range(9):
        if board[r][c]=='.':
          for i in range(9):
            v=chr(ord('1')+i)
            if rowlacks(r,v) and collacks(c,v) and sublacks(r,c,v):
              board[r][c]=v
              if _ss():
                return True
              board[r][c]='.'
          return False      
    return True
  
  return _ss()
        
board=[
  [".",".",".","7",".",".","3",".","1"],
  ["3",".",".","9",".",".",".",".","."],
  [".","4",".","3","1",".","2",".","."],
  [".","6",".","4",".",".","5",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".","1",".",".","8",".","4","."],
  [".",".","6",".","2","1",".","5","."],
  [".",".",".",".",".","9",".",".","8"],
  ["8",".","5",".",".","4",".",".","."]]

print(sudoku_solve(board))'''
basic idea, set a cell only to a valid value
valid means the sub doesn't have it, and the row and col don't have it

opts={(0,2):12345679,(0,4):...,}

for any cell, for each valid opt
  put that there (backtracking),
  if we can fill the board the answer is true. otherwise false
  
'''
def sudoku_solve(board):
  def printboard():
    for r in board:
      print(''.join(r))
    print('\n\n')
    
  def rowlacks(r,v):
    for c in range(9):
      if board[r][c]==v:
        return False
    return True
  
  def collacks(c,v):
    for r in range(9):
      if board[r][c]==v:
        return False
    return True

  def sublacks(r,c,v):
    sc=(c//3)*3
    sr=(r//3)*3
    for i in range(3):
      for j in range(3):
        if board[sr+i][sc+j]==v:
          return False
    return True
  
  def _ss(r,c):
    if c==9:
      r,c=r+1,0
    if r==9:
      return True

    if board[r][c]!='.':
      return _ss(r,c+1)
      
    if board[r][c]=='.':
      temp=board[r][c]
      for i in range(9):
        v=chr(ord('1')+i)
        if rowlacks(r,v) and collacks(c,v) and sublacks(r,c,v):
          board[r][c]=v
          if _ss(r,c+1):
            return True
      board[r][c]=temp
    return False
  
  return _ss(0,0)
        
board=[
  [".",".",".","7",".",".","3",".","1"],
  ["3",".",".","9",".",".",".",".","."],
  [".","4",".","3","1",".","2",".","."],
  [".","6",".","4",".",".","5",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".","1",".",".","8",".","4","."],
  [".",".","6",".","2","1",".","5","."],
  [".",".",".",".",".","9",".",".","8"],
  ["8",".","5",".",".","4",".",".","."]]

print(sudoku_solve(board))'''
brute force put all possibilities in the board; then test for validity (9**n) where n is number of empty cells. storage: 9*9, because call stack is board size
better: fill a cell. immediately check for validity, then proceed. still 9**n but will avoid unnecessary tables generated, when in linear time could have validated immediately!

if i am at a cell, try 
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def rowlacks(r,v):
            return v not in board[r]

        def collacks(c,v):
            return v not in (board[i][c] for i in range(9))

        def sublacks(r,c,v):
            sr,sc=(r//3)*3,(c//3)*3
            for i in range(3):
                for j in range(3):
                    if board[i+sr][j+sc]==v:
                        return False
            return True

        def ss(r,c):
            if c==9:
                r,c=r+1,0
            if r==9:
                return True
            if board[r][c]!='.':
                return ss(r,c+1)
            for i in range(9):
                v=chr(ord('1')+i)
                if rowlacks(r,v) and collacks(c,v) and sublacks(r,c,v):
                    board[r][c]=v
                    if ss(r,c+1):
                        return True
            board[r][c]='.'
            return False

        ss(0,0)
        '''
for each cell that is a ., try all 1-9, and call one cell forward
if nothing left return True. 
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def valid(ch,r,c):
            for i in range(9):
                if ch in (board[i][c], board[r][i]):
                    return False
            sr=r//3*3
            sc=c//3*3
            for i in range(3):
                for j in range(3):
                    if ch == board[sr+i][sc+j]:
                        return False
            return True

        def solveSudoku():
            for r in range(9):
                for c in range(9):
                    if board[r][c]=='.':
                        for i in range(1,10):
                            ch=str(i)
                            if valid(ch,r,c):
                                board[r][c]=ch
                                if solveSudoku():
                                    return True
                        board[r][c]='.'
                        return False
            return True

        solveSudoku()'''
for each cell that is a ., try all 1-9, and call one cell forward
if nothing left return True. 
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def valid(ch,r,c):
            for i in range(9):
                if ch in (board[i][c], board[r][i]):
                    return False
            sr=r//3*3
            sc=c//3*3
            for i in range(3):
                for j in range(3):
                    if ch == board[sr+i][sc+j]:
                        return False
            return True

        def solveSudoku(r,c):
            if c==9:
                r,c=r+1,0
            if (r,c)==(9,0):
                return True

            if board[r][c]!='.':
                return solveSudoku(r,c+1)
            for i in range(1,10):
                ch=str(i)
                if valid(ch,r,c):
                    board[r][c]=ch
                    if solveSudoku(r,c+1):
                        return True
            board[r][c]='.'
            return False

        solveSudoku(0,0)