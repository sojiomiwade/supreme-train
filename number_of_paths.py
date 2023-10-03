def num_of_paths_to_dest(n):
  def helper(row, col):
    if (row,col) in memo:
      return memo[row,col]
    if (row, col) == (n-1, n-1):
      memo[row,col] = 1
      return 1
    if row > col or col > n-1:
      memo[row,col] = 0
      return 0    
    memo[row,col] = helper(row + 1, col) + helper(row, col + 1)  
    return memo[row,col]
  memo = {}
  return helper(0, 0)

print(num_of_paths_to_dest(50)) #1
