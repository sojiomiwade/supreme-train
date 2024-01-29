def find_array_quadruplet(arr, s):
  '''
  sort the array
  1 4 5 8 9 ...
  x+y+z1+z2=20
  target=20-(x+y)
  z2= target  - z1
  x, y, 
    for z1, find z2 with twosum against 20
  for i
  order should come without any additional ops because we sorted  
  '''
  arr.sort()
  n=len(arr)
  for i in range(n):
    for j in range(i+1,n):
      x,y=arr[i],arr[j]
      target=s-(x+y)
      left,right=j+1,n-1
      while left<right:
        a,b=arr[left],arr[right]
        if a+b==target:
          return [x,y,a,b]
        if a+b<target:
          left+=1
        else:
          right-=1
  return []
'''
0,1,2,3,4,6,7,8,9
i       j l     r 
target=20-4=16
15==16 good.
'''        
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
output=[0,4,7,9]
print(find_array_quadruplet(arr, s))
assert find_array_quadruplet(arr, s)==output

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = -1
output=[]
print(find_array_quadruplet(arr, s))
assert find_array_quadruplet(arr, s)==output

arr = [1,1,1,1,0,0,0,4]
s = 4
output=[0,0,0,4]
assert find_array_quadruplet(arr, s)==output

arr = [0,0,0,4]
s = 4
output=[0,0,0,4]
assert find_array_quadruplet(arr, s)==output
