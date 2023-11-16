'''
in a canvas, draw a line from a point x to a point y

x
 x
   x
    xxxxy

11111111111

            s
           s
          s
         s
fssssssss

f=(fx,fy)
s=(sx,sy)

1)move in x and y dir until either sx equals fx or sy=fy

now 2 can be unnecessary if we let 1 have a zero dir and we don't stop until (sx,fx)==(sy,fy)
2)then move in the not equal to dir till you get there
    two while loops, one for each axis
'''

#time,space: n**2,1
def print_canvas(canvas):
    for r in canvas:
        print(''.join(str(val) for val in r))
    print()

#time,space: n,1
def link(sx,sy,fx,fy,canvas):
    while (sx,sy) != (fx,fy):
        canvas[sy][sx]=1
        xdir=0
        if sx<fx:
            xdir=1
        elif sx>fx:
            xdir=-1
        ydir=0
        if sy<fy:
            ydir=1
        elif sy>fy:
            ydir=-1
        sx+=xdir
        sy+=ydir
    canvas[sy][sx]=1

n=10
canvas=[[0 for _ in range(n)] for _ in range(n)]
print_canvas(canvas)
link(0,0,5,5,canvas)
link(0,0,0,5,canvas)
link(5,5,0,5,canvas)
print_canvas(canvas)
