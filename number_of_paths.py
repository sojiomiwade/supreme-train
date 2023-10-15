def num_of_paths_to_dest(n):
  def helper(row, col):
    if (row, col) == (n-1, n-1):
      return 1
    if row > col or col > n-1:
      return 0    
    if (row,col) in memo:
      return memo[row,col]
    memo[row,col] = helper(row + 1, col) + helper(row, col + 1)  
    return memo[row,col]
  memo = {}
  return helper(0, 0)

print(num_of_paths_to_dest(50)) #1
def num_of_paths_to_dest(n):
  def valid(row, col):
    return row <= col and col < n
  def dfs(row, col): # 01->11
    if not valid(row, col):
      return 0
    if row == col == n-1:
      return 1
    if (row,col) in cache:
      return cache[row,col]
    cache[row,col] = dfs(row + 1, col) + dfs(row, col + 1)
    return cache[row,col]
  cache = {}
  return dfs(0,0)
  
n = 4
print(num_of_paths_to_dest(n))