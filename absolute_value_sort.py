def absSort(arr):
  """
  @param arr: int[]
  @return: int[]
  """
  arr.sort(key=lambda x: (abs(x),x))
  return arr