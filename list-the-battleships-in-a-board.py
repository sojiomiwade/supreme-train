'''
https://leetcode.com/discuss/interview-question/618999/Facebook-or-Phone-or-Battleships-or-where-did-i-go-wrong
The question was similar to battleships on the board, but I was asked to return the coordinates
for example we have

[["X",".",".","X"],
 [".",".",".","X"],
 [".",".",".","X"]]
You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships

output should be [[(0,0),] [(0,3), (1,3), (2,3)]] representing 2 ships on the board

create sl lookup with default dict of list
if this is a 'X'
    if there is a prior one get it (left or right) as ship
    otherwise create one ship: 
        ship=sl[this point]
'''

from collections import defaultdict
from typing import List, Tuple


def get_ships(board: List[List[str]]) -> List[Tuple[Tuple]]:
    sl=defaultdict(list)
    m,n=len(board),len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j]=='X':
                if i-1>=0 and board[i-1][j]=='X':
                    sl[i,j]=ship=sl[i-1,j]
                elif j-1>=0 and board[i][j-1]=='X':
                    sl[i,j]=ship=sl[i,j-1]
                else:
                    ship=sl[i,j]
                ship.append((i,j))
    return  list(set(tuple(lis) for lis in sl.values()))

'''
sl {00:[00],  03,13,23,:[03 13 23]}
'''
board=[
 ["X",".",".","X"],
 [".",".",".","X"],
 [".",".",".","X"]]
print(get_ships(board))
#exp [00], [03 13 23]