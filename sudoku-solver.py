'''
7 2 5 4 3 5(no)
principles:
    - when we backtrack, we must return the dot back!
    - we go forward only because the current was valid
operatioin: 
    if dot
        for all possible numbers, put the number, and call forward
        if we get back a true, return that
        otherwise keep trying numbers
    revert the dot
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def valid(num:str, r: int, c: int) -> bool:
            for k in range(9):
                if board[r][k]==num or board[k][c]==num:
                    return False
            # 5->3, (6,7)->6 ... 5//3=1, 1*3 = 3
            # r (or c) --> (r//3)*3
            sr,sc=(r//3)*3,(c//3)*3
            for i in range(sr,sr+3):
                for j in range(sc,sc+3):
                    if board[i][j]==num:
                        return False
            return True

        def solveit(r: int, c: int) -> bool:
            if c==9:
                r,c=r+1,0
            if r==9:
                return True
            if board[r][c]!='.':
                return solveit(r,c+1)
            for numi in range(1,10):
                num=str(numi)
                if valid(num,r,c):
                    board[r][c]=num
                    if solveit(r,c+1):
                        return True
            board[r][c]='.'
            return False


        solveit(0,0)