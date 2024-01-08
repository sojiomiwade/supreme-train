'''
all dfs paths from (0,0) to (n-1,n-1)
but i>=j must always hold
recursively get to destination, and increment count
backtrack for more counts

at a node (x,y), can do x+1,y or x,y+1
return the sum of the return values
within the function check if valid and return 0 if not
if at destination, return 1  
'''
def num_of_paths_to_dest(n):
  def numpaths(x,y):
    if x<y or x==n or y==n:
      return 0
    if (x,y)==(n-1,n-1):
      return 1
    if (x,y) in dp:
      return dp[x,y]
    dp[x,y]=numpaths(x+1,y)+numpaths(x,y+1)
    return dp[x,y]
  dp={}
  return numpaths(0,0)
  
print(num_of_paths_to_dest(3)) #2
print(num_of_paths_to_dest(2)) #1