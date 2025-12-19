'''
ABCDEFG
  i
ABDFFGH
  j

AB -C D -E

train : 00 -> 11 -> 22 -> 32 -> ... -> mn

once it comes back: next(22)=32

if (i+1) j, then '-s[i]'
else +t[j]

A
A
00 -> 11
a
 i
ab
 j
 
 
'''
def diffBetweenTwoStrings(source, target):
  def diff(i, j):
    if i==m or j==n:
      return max(n-j,m-i)
    if (i,j) in dp:
      return dp[i,j]
    if source[i]==target[j]:
      dp[i,j]=diff(i+1,j+1)
      nexttup[i,j]=(i+1,j+1)
    else:
      delsourcedist=diff(i+1,j)
      addtargetdist=diff(i,j+1)
      if delsourcedist<=addtargetdist:
        dp[i,j]=1+delsourcedist
        nexttup[i,j]=(i+1,j)
      else:
        dp[i,j]=1+addtargetdist
        nexttup[i,j]=(i,j+1)
    return dp[i,j]

  '''
  actually do have to finish out the i and the j
  ABCDEFG
   i
   j
  A
  -b -c -d -e ...
  
  AC
   i
   j
  ABQ
  00 
  ans=[A -C +B +Q +R +S]
  '''
  m,n=len(source),len(target) 
  dp={}
  nexttup={}
  diff(0,0)
  i=j=0
  ans=[]
  while i<m and j<n:
    ni,nj=nexttup[i,j]
    if (ni,nj)==(i+1,j+1):
      ans.append(source[i])
      i,j=i+1,j+1
    elif (ni,nj)==(i+1,j):
      ans.append('-'+source[i])
      i+=1
    else:
      ans.append('+'+target[j])
      j+=1
  for k in range(i,m):
    ans.append('-'+source[k])
  for k in range(j,n):
    ans.append('+'+target[k])
  return ans

source,target='AC','ABQ'
print(diffBetweenTwoStrings(source, target))