'''
3sum equal to s
c=arr[i]
a+b+c=s
a+b+(c-s)
for i in range(s):
  twosum(i)


find 3sum equal to s
  a+b=s-arr[i]
  a+b+arr[i]=s
  for each idx i
    if 2sum(i,s)
  2sum(i,s): 
    excluding idx i
    can find two numbers equal to s-arr[i]
  
find 4sum equal to s
  a+b=s-arr[i]-arr[j]
  
[0 2 4 7 9]
2 4 4 4
  i j k
'''
def find_array_quadruplet(arr, s):
  def twosum(i,j):
    have=set()
    for k in range(n):
      if j<k:
        if s-arr[i]-arr[j]-arr[k] in have:
          return s-arr[i]-arr[j]-arr[k],arr[k]
        have.add(arr[k])
    return None,None
  
  n=len(arr)
  if n<4: 
    return []
  arr.sort()
  for i in range(n):
    for j in range(n):
        if i<j:
          c,d=twosum(i,j)
          if c is not None:
            return [arr[i],arr[j],c,d]
  return []
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print(find_array_quadruplet(arr, s)) # [0479]