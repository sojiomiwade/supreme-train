'''
       t
[1, 2, 3, 5, 6, 7]
[3, 6, 7, 8, 20]
 b
 if the same, stash it, and advance any or both
 otherwise advance the pointer smaller. when you reach the 
 end of one you are done. time and space: O(n + m), O(1)
 
 approach 2. bin search on array 2 repeatedly for all elements in arr 1
 time and space: O(n * lg m), O(1)
 
 t
 1 2
 1 8
 b
'''
def find_duplicates(arr1, arr2):
  def binsearch(key, arr, start):
    lo, hi = start, len(arr) - 1
    while lo <= hi:
      mi = lo + (hi - lo) // 2
      if arr[mi] == key:
        return mi
      if arr[mi] > key: # 1 30 50
        hi = mi - 1
      else:
        lo = mi + 1
    return -1
  
  res = []
  loc = -1
  for el in arr1:
    found = binsearch(el, arr2, loc + 1)
    if found != -1:
      loc = found
      res.append(el)
  return res
  '''
  n, m = len(arr1), len(arr2)
  t = b = 0
  res = []
  while t < n and b < m:
    if arr1[t] == arr2[b]:
      res.append(arr1[t])
      t += 1
      b += 1
    elif arr1[t] < arr2[b]:
      t += 1
    else:
      b += 1
  return res
  '''
