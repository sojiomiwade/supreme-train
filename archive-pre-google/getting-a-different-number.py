'''
0 2 5 7 8 
  ^
sort then find the first: O(n lg n) + O(1)
5 2 7 0 8 | 1
1 2 3 4 5 | 6
0 1 2 3 4 | 5

9 3 8 4 
ans 8 2 

9 8 1 2 7 0 5
          ^ 0 needs to know that 1 is not in the array
ans 8
ans 6 3 1  
have 9 8 1 2. simple: 
operation: check if elem+1 is not in have, you can set ans to min(ans,elem+1). regardless add elem to have

0 1 2 <-- corner
5 2 7 <-- simple
have 
ans 0
0 1 2
20 m first solution. now let's modify only the existing array => O(1) space
0 1 2 7 8 5
0 1 2 3 4 5

    5   2       
0 1 2 3 4
put each element in its place:
  keep putting other elements in their place, until you find yours. 
  if element is bigger or equal to arr size, move on
  then loop again in arr to see first element not in place
'''
def get_different_number(arr):
  for i,elem in enumerate(arr):
    while elem<len(arr) and i!=elem: # 4!=2
      arr[elem],arr[i]=elem,arr[elem] # a[2],a[4]=2,5
      elem=arr[i]
  for i,elem in enumerate(arr):
    if i!=elem:
      return i
  return len(arr)
  '''
  have=set(arr)
  for ans in range(len(arr)):
    if ans not in have:
      return ans
  return len(arr)
  '''
