'''
in a canvas, draw a line from a point x to a point y
DON'T LOOK BELOW. IT'S GOT A SOLUTION OUTLINE




deltax is 1 or -1 depending on if startx < or > finishx
likewise deltay
curx,cury=startx,starty
arr[curx][cury]=.
loop until we are at finish y and finishx as follows
    if curx is already at finishx, do nothing to it
    otherwise increment it with deltax
    likewise cury
    arr[curx][cury]=.
return arr
'''


from typing import Tuple


def draw(start: Tuple[int,int], end: Tuple[int,int]) -> None:
    ...