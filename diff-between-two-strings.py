def diffBetweenTwoStrings(source, target):
  def dd(i, j):
    if (i,j) in dp:
      return dp[i,j]
    eqval=float('inf')
    if source[i]==target[j]:
      eqval=dd(i+1,j+1)
    dp[i,j]=min(eqval,1+dd(i+1,j),1+dd(i,j+1))
    return dp[i,j]
  
  dp={}
  m, n = len(source), len(target)
  for i in range(m):
    dp[i,n]=m-i
  for j in range(n):
    dp[m,j]=n-j
  dp[m,n]=0
  dd(0,0)
  ans=[]
  i=j=0
  
  '''
      i
  1 Q 2 3 E 1 2 3 
  Q 
    j
  '''
  while i<m and j<n:
    if source[i]==target[j]:
      ans.append(source[i])
      i+=1
      j+=1
    else:
      if dp[i,j+1]<dp[i+1,j]:
        ans.append('+'+target[j])
        j+=1
      else:
        ans.append('-'+source[i])
        i+=1
  for ri in range(i,m):
    ans.append(f'-{source[ri]}')
  for rj in range(j,n):
    ans.append(f'+{target[rj]}')
  return ans

'''
  print(len(dp),m*n)
  assert len(dp) == m * n
  for i in range(m):
    for j in range(n):
      print (dp[i,j],end=' ')
    print()
'''

source, target = 'CDE','DFF'
'''
A B C D E F G
A B D F F G H
A A -C D -E F +F G +H
'''
source, target = 'G','FGH'
res=diffBetweenTwoStrings(source, target)
exp=['+F', 'G', '+H']
assert exp==res
# print(diffBetweenTwoStrings(source, target))
source, target = 'ABCDEFG','ABDFFGH'
exp=['A', 'B', '-C', 'D', '-E', 'F', '+F', 'G', '+H']
res=diffBetweenTwoStrings(source, target)
assert exp==res
# print(res)
