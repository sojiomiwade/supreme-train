'''
The question was similar to battleships on the board, but I was asked to return the coordinates
for example we have

You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships

output should be [(0,0)] [(0,3), (1,3), (2,3)] representing 2 ships on the board

'''
from typing import List, Tuple


def get_b_coords(grid: List[List[str]]) -> List[List[Tuple[int, int]]]:
    '''
    if i am part of a battleship, then i should be added to some list. 
    which one? the one above me
    '''
    m, n = len(grid), len(grid[0])
    ship_lookup = {}
    for r in range(m):
        for c in range(n):
            delta_row = delta_col = 0
            if grid[r][c] == 'X':
                if r > 0 and grid[r - 1][c] == 'X':
                    delta_row = 1
                elif c > 0 and grid[r][c - 1] == 'X':
                    delta_col = 1

                if delta_row or delta_col:
                    ship_lookup[r, c] = ship_lookup[r - delta_row, c - delta_col]
                    ship_lookup[r, c].append((r,c))
                else:
                    ship_lookup[r, c] = [(r,c)]
    ans = set()
    for ship in ship_lookup.values():
        ans.add(tuple(ship))
    return list(ans)

# lookup = {(0,0):[(0,0)], (0,2):[(0,2),(1,2)]}

grid1 = [
    ["X",".","X"],
    [".",".","X"]]
print(get_b_coords(grid1))

grid2 = [
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]]
print(get_b_coords(grid2))
