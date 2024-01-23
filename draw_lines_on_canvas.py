'''
in a canvas, draw a line from a point x to a point y

x
 x
   x
    xxxxy

s          
          
  x       
      f    
  f
step in the row and col dir until we are in the row or col.
then (i) march to the row and (ii) then to the col
3 loops in all
''' 
from typing import List

SET=1
CLEAR=0
def draw(sr: int, sc: int, fr: int, fc: int, canvas: List[List[int]]) -> None:
    m,n=len(canvas),len(canvas[0])
    for x in sr,sc:
        assert x>=0
    for r,c in zip((sr,sc),(fr,fc)):
        for x,ub in zip((r,c),(m,n)):
            assert x<ub, f'need {x} < {ub}'
    r,c=sr,sc
    rowadvance=coladvance=1
    if sr>fr:
        rowadvance=-1
    if sc>fc:
        coladvance=-1
    while True:
        canvas[r][c]=SET
        if r==fr or c==fc:
            break
        r+=rowadvance
        c+=coladvance
    sr,sc=r,c
    for r in range(sr,fr+rowadvance,rowadvance):
        canvas[r][sc]=SET
    for c in range(sc,fc+coladvance,coladvance):
        canvas[sr][c]=SET

m,n=10,20
canvas=[[CLEAR for _ in range(n)] for _ in range(m)]
draw(1,1,5,5,canvas)
draw(0,3,2,10,canvas)
draw(5,5,0,5,canvas)
draw(9,0,5,3,canvas)
# draw(20,20,0,5,canvas)

for r in range(m):
    print(''.join(str(canvas[r][c]) for c in range(n)))
