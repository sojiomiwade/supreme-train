'''
first: consider all pairs x!=y: x-y=k. time,space:n**2,1
better:
k=1
1 0 -> [1,0] 
0 1 -> [1,0]
x - y = k  or y - x = k
x-k (add (x,y)) or x+k (add (y,x)) we already have

ans should be [[1,0]]
arr=[1 0] k=1
     x
have:{1 }
ans:[[1,0]]

{2}
=>
'''
def find_pairs_with_given_difference(arr, k):
  have={}
  ans=[]
  for i,x in enumerate(arr):
    if x-k in have:
      ans.append([x,x-k])
    if x+k in have:
      ans.append([x+k,x])
    have[x]=i
  ans.sort(key=lambda tup: have[tup[1]])
  return ans
arr,k=[0, -1, -2, 2, 1],1
print(find_pairs_with_given_difference(arr, k))