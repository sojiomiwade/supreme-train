"""
@param S: str
@return: int

          1262
       1       12
   2      26
 6   62x
2  x
 2

1         12
12 126    126 1262
           1262
    1      262
  2       2 62
  6 
  2
          /
    1262 --> 3
      i
    1 2 6 2 
    gc=1
"""
def decodeVariations(S):
  def decode(idx):
    if idx==n:
      return 1
    if idx in dp:
      return dp[idx]
    count=0
    val1=int(S[idx])
    if val1!=0:
      count=decode(idx+1)
    val2=int(S[idx:idx+2])
    if 10<=val2<=26:
      count+=decode(idx+2)
    dp[idx]=count
    return dp[idx]
  
  dp={}
  n=len(S)
  return decode(0)
