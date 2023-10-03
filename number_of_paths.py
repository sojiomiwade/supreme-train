def num_of_paths_to_dest(n):
  def helper(row, col, count): #01 11
    if (row, col) == (n-1, n-1):
       return count
    if row < n and row >= col + 1: # 0 >= 0+1: 0 < 2 0 >= 11
      count += helper(row + 1, col, count + 1)     
    if col < n: # 0 < 
      count += helper(row, col + 1, count + 1) #
    return count
  
  return helper(0, 0, 0)
