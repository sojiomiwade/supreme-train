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

print(sudoku_solve(board))