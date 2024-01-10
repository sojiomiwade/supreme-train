'''
      D F F
      0 1 2 | 3
---------------
C 0 | 4 5 4 | 3   
D 1 | 3 4 3 | 2   
E 2 | 4 3 2 | 1
---------------
  3 | 3 2 1 | 0   
  4 | i i i |
-C D -E +F +F = 4

move in j implies deleting from destination (+ dst character)
move in i implies deleting from source (+ source chractor) -- l
move in both implies keep that char

first check if the two are the same:
if so, then add just the char (i,j)
if 

dd(i,j)=min(dd(i,))
move in j implies deleting from destination (+ dst character)
move in i implies deleting from source (+ source chractor) -- l
move in both implies keep that char

D F
D F F
'''
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
  
  while i<=m and j<n:
    if i<m and source[i]==target[j]:
      ans.append(source[i])
      i+=1
      j+=1
    else:
      if i==m or dp[i,j+1]<dp[i+1,j]:
        print(j,'j')
        ans.append('+'+target[j])
        j+=1
      else:
        ans.append('-'+source[i])
        i+=1        
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
source, target = 'ABCDEFG','ABDFFGH'
#print(source, target)
#print(diffBetweenTwoStrings(source, target))
