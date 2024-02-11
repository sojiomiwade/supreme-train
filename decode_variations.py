"""
@param S: str
@return: int

dv(i) = (cond(i) and dv(i+1)) +  (cond(i:i+2) and dv(i+2))

1 --  1
      |
      v
12 -- 1 + 1


12
ab
l

122 - 2
abb
lb
av

vwxyz
cond(i) ok => take dp[i-1]
cond([i-1..i]) ok => add on dp[i-2]
       1 2 6 2
  1 1  . . . .
dv(i) = (cond(i) and dv(i+1)) +  (cond(i:i+2) and dv(i+2))
 1 2
"""
	
def decodeVariations(S):
  n=len(S)
  dp=[0]*(n+2)
  dp[0]=dp[1]=1
  for i in range(2,n+2):
    val1=0
    if 1<=int(S[i-2])<=9:
      val1=dp[i-1]
    val2=0
    if 10<=int(S[max(0,i-3):i-1])<=26: #-1..0  ->  [-1:1] .. -1:1  --> 
      val2=dp[i-2]
    dp[i]=val1+val2
  return dp[-1]

S='1262'
print(decodeVariations(S)) # 3