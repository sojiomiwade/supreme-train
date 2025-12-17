'''
2 7 4 0 9 5 1 3
l
r

0 1 2 3 4 5 7 9
a
      b
  c         d 
  
0 2 4 7 9 | s 20 | ans [0 4 7 9]
a
    b
      c
        d
target = 18
find c and d where sum target is 20 - (a+b)
then sort the ans
'''
def find_array_quadruplet(arr, s):
  arr.sort()
  n=len(arr)
  for a in range(n):
    for b in range(a+1,n):
      target=s-(arr[a]+arr[b])
      c,d=b+1,n-1
      while c<d:
        if arr[c]+arr[d]==target:
          return [arr[i] for i in (a,b,c,d)]
        elif arr[c]+arr[d]<target:
          c+=1
        else:
          d-=1
  return []        