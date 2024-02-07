'''
try every number in cells that are not already marked

0 1 2 -> 0
3,4,5 -> 3
678 -> 6
7//3=2
2*3

(r//3)*3 

5//3=1

6
'''
def solution(sudoku):
    def lacks(r,c,val):
        for i in range(n):
            if sudoku[i][c]==val or sudoku[r][i]==val:
                return False
        sc=(c//3)*3
        sr=(r//3)*3
        for i in range(3):
            for j in range(3):
                if sudoku[sr+i][sc+j]==val:
                    return False
        return True
        
    def help(r: int, c: int) -> bool:
        if c==n:
            r,c=r+1,0
        if r==n:
            return True
        if sudoku[r][c]!=0:
            return help(r,c+1)

        for i in range(n):
            if lacks(r,c,1+i):
                sudoku[r][c]=1+i
                if help(r,c+1):
                    return True
        sudoku[r][c]=0
        return False
            
    n=9
    solved=help(0,0)
    assert solved
    return sudoku


# sudoku=[[5,3,4,6,7,8,9,1,2], 
#  [6,7,2,1,9,5,3,4,8], 
#  [1,9,8,3,4,2,5,6,7], 
#  [8,5,9,7,6,1,4,2,3], 
#  [4,2,6,8,5,3,7,9,1], 
#  [7,1,3,9,2,4,8,5,6], 
#  [9,6,1,5,3,7,2,8,4], 
#  [2,8,7,4,1,9,6,3,5], 
#  [3,4,5,2,8,6,1,7,9]]
        
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

n=9
sudoku=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]!='.':
            sudoku[i][j]=int(board[i][j])
print(solution(sudoku))
