# can just use x>0 for 2nd tuple item
def absSort(arr):
  arr.sort(key=lambda x:(abs(x), 0 if x < 0 else 1))
  return arr
