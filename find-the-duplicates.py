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
'''
n~m => we go for n+m 
1 2 3 4 5 6 7
              i
      j
3 6 7 8 20
res = 3 6 7
if elemens of idxs are the same, advance both pointers
othewise, advance the pointer to the smaller value

1 2 3
    i
    j
0 2
res = 2 
'''
def find_duplicates(arr1, arr2):
  N, M = len(arr1), len(arr2)
  i = j = 0
  res = []
  while i < N and j < M:
    if arr1[i] == arr2[j]:
      res.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] < arr2[j]:
      i += 1
    else:
      j += 1
  return res

# now we go for binary search on the bigger
'''
1 2 3 4 5 6 7
    l
    m    
    h
3 7
k
res = 3
complexity = min(N,M) * lg(max(N,M))
'''
def find_duplicates(arr1, arr2):
  res = []
  if len(arr1) > len(arr2):
    arr1, arr2 = arr2, arr1
  for key in arr1:
    lo, hi = 0, len(arr2)-1
    while lo <= hi:
      mi = lo + (hi - lo) // 2
      if arr2[mi] == key:
        res.append(key)
        break
      if arr2[mi] > key:
        hi = mi - 1
      else:
        lo = mi + 1
  return res