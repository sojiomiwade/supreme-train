'''
x-y=k
x, look for x-k in arr
*also* look for y+k in arr

arr 2 1 3 0 
k 1
1 2
0 1
2 3
-1 0
ans [ 3,2 2,1 1,0]
'''
def find_pairs_with_given_difference(arr, k):
  ans=[]
  xval={}
  for x in arr:
    xval[x-k]=x
  for y in arr:
    if y in xval:
      ans.append([xval[y],y])
  return ans