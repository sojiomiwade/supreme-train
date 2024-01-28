25
16 + 8 + 1
11001
ans=10011
approach:

n=|11001
ans=19 == 10011
while n
  ans = 2*ans + (n&1)
  n>>=1
return ans