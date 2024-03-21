'''
idea look to left and up for  visited. if so cannot count this if it is an X
X .
X .
count 1
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count=0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c]=='X' and 
                    (r==0 or board[r-1][c]!='X') and 
                    (c==0 or board[r][c-1]!='X')):
                    count+=1
        return count