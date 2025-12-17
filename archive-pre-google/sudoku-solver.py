'''
. . .
. 5 .
2 . .
filled slots are pass-through
others iterate through all numbers seeking validity
  before putting a char, ensure it isn't violating
  at the end of a row, be sure to move to next row
if row,col is 10,1, then can return True
row = 6, col 7
6//3 = 2
2 * 3 = 6

7//3 = 2
2*3 = 6
'''
def sudoku_solve(board):    
  def solve(row, col):
    def valid():
      for k in range(9):
        if ch in (board[row][k],board[k][col]):
          return False
      srow,scol=(row//3)*3,(col//3)*3
      for r in range(srow,3+srow):
        for c in range(scol,3+scol):
          if ch==board[r][c]:
            return False
      return True
    
    if col==9:
      row,col=row+1,0
    if (row,col)==(9,0):
      return True
    
    if board[row][col]!='.':
      return solve(row,col+1)
    
    for i in range(1,10):
      ch=str(i)
      if valid():
        board[row][col]=ch
        if solve(row,col+1):
          return True
        board[row][col]='.'
    return False
    
  return solve(0,0)