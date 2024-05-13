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
  ts,vcount,enteredj=data[0]
  maxvcount,maxts=float('-inf'),data[0]
  i,j,n=0,0,len(data)
  netvcount=0
  while i<n:
    ts,_,_=data[i]
    while j<n and data[j][0]==ts:
      tsj,vcountj,enteredj=data[j]
      if enteredj==1:
        netvcount+=vcountj
      else:
        netvcount-=vcountj
      j+=1
    if netvcount>maxvcount:
      maxts=ts
      maxvcount=netvcount
    i=j
  assert maxts is not None
  return maxts