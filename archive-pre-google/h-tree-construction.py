'''
all three line segments are the same length
can be an input parameter, SEGLEN
at any depth, just draw four h-trees
recursive terminal condition will stop fturue trees
term cond: if dep==0 return
d(1)
'''

def drawHTree(x, y, length, depth):
  def drawLine(*args):
    assert len(args)==3
    print(depth-args[-1])
    print((depth-args[-1])*' '+'-'.join(str(tup) for tup in args[:-1]))

  def drawtree(x, y, length, dep):
    if dep:
      halfl=length/2
      xl,xr=x-halfl,x+halfl
      yb,yt=y-halfl,y+halfl
      drawLine((xl,y),(xr,y),dep)
      drawLine((xl,yt),(xl,yb),dep)
      drawLine((xr,yt),(xr,yb),dep)
      
      dep-=1
      length/=pow(2,.5)
      drawtree(xl,yt,length,dep)
      drawtree(xl,yb,length,dep)
      drawtree(xr,yt,length,dep)
      drawtree(xr,yb,length,dep)

  drawtree(x,y,length,depth)

s=3*' '
print len(s),s+'hello'
#drawHTree(0,0,100,2)