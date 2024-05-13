"""
[ts,vcount,entered]
[int,int,int]

151 251 230 311 
            i
            j
tsj,vcountj,enteredj 151
maxvcount, maxts 5,1
netvcount 2
for each timestamp, get its net, then update maxcount, and maxts
time complexity is just the size of data
space is O(1)
"""
def find_busiest_period(data):
  maxvcount,maxts=float('-inf'),None
  i,j,n=0,0,len(data)
  prev=0
  while i<n:
    ts,_,_=data[i]
    netvcount=0
    while j<n and data[j][0]==ts:
      tsj,vcountj,enteredj=data[j]
      if enteredj==1:
        netvcount+=vcountj
      else:
        netvcount-=vcountj
      j+=1
    if netvcount-prev>maxvcount:
      maxts=tsj
      maxvcount=netvcount
    prev=netvcount
    i=j
  assert maxts is not None
  return maxts