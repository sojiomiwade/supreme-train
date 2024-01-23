'''

'''
def drawline(x1,y1,x2,y2):
  print((x1,y1),(x2,y2))
def draw(x,y,length,depth):
  if depth==0:
    return
  # 3 lines
  half_l=length/2
  xleft,xright=x-half_l,x+half_l
  ytop,ybot=y+half_l,y-half_l
  drawline(xleft,y,xright,y)
  drawline(xleft,ytop,xleft,ybot)
  drawline(xright,ytop,xright,ybot)
    
  #call 4 draws
  sqrt2=2**(.5)
  nl=length/sqrt2
  draw(xleft,ytop,nl,depth-1)
  draw(xleft,ybot,nl,depth-1)
  draw(xright,ytop,nl,depth-1)
  draw(xright,ybot,nl,depth-1)

draw(100,100,100,2)
#(50,100),(150,100)
#(50,50),(50,150)
#(150,50),(150,150)

nl=100/(2**.5)
print(50-nl/2)