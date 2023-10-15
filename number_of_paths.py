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


'''
now tabulate...
r>0, c>0

  0 1 2 3 4
4 x x x x 14
3 x x x 5 14
2 x x 2 5 9
1 x 1 2 3 4
0 1 1 1 1 1

  0 0
  1 1
'''
def num_of_paths_to_dest(n):
  tab = [[1 if i==0 else 0 for j in range(n)] for i in range(n)]
  for r in range(1,n):
    for c in range(r,n):
      tab[r][c] = tab[r-1][c] + tab[r][c-1]
  return tab[n-1][n-1]
n = 5

print(num_of_paths_to_dest(n))


'''
using linear space cache
'''
def num_of_paths_to_dest(n):
  def valid(row, col):
    return row <= col and col < n
  def dfs(row, col, incache):
    if not valid(row, col):
      return 0
    if row == col == n-1:
      return 1    
    if cache[col] != 0 and incache != False:
      return cache[col]
    cache[col] = dfs(row + 1, col, incache=None) + dfs(row, col + 1, incache=False)
    return cache[col]
  cache = [0 for _ in range(n)]
  
  return dfs(0, 0, None)

n = 20
print(num_of_paths_to_dest(n))
