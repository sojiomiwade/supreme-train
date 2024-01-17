"""
2 ->2,1
-2->2,0
-7->7,0
0 ->0,0
"""

def absSort(arr):
  return sorted(arr,key=lambda x: (abs(x),x>0))

arr = [2, -7, -2, -2, 0]
print(absSort(arr))