'''
 0  1 2 3 4 5 6 7
-8  0 2 5 6 7 8 9
      ^

 0  1 2 3 4 5 6 7
-8  0 2 5 6 7 8 9

 0 1 2 3 4 5 6 7
 - - - - - 5 6 7
 
  0 1 2 3
 -1 0 3 6
 lo,hi 2,1
 mi 2
 if idx bigger than a[idx], remove the left of the array  <-- right can have it
 idx smaller than a[idx], remove right side of array      <--- right can never have ans
 if equality i==a[i], save ans, but remove i to right of array <-- we want better
'''
def index_equals_value_search(arr):
  ans=-1
  lo,hi=0,len(arr)-1
  while lo<=hi:
    mi=lo+(hi-lo)//2
    if mi==arr[mi]:
      ans=mi
      hi=mi-1
    elif mi>arr[mi]:
      lo=mi+1
    else:
      hi=mi-1
  return ans