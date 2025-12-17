'''
lowercase latin characters only

ans[i]=w[i]-w[i-1]
ans[0] is just ans[0]-1
then do the 26 thing to get it to ascii for each one
  add 26 until we have 97<=x<=123
113-116=-3
-3
26
23
26
49
26
75
26
101 --> convert to ascii

94+

'''
def decrypt(word):
  ans=[]
  n=len(word)
  ALPHALEN=26
  FIRST,LAST=97,122 #0 26
  for i in range(n-1,-1,-1):
    op2=ord(word[i-1]) if i-1>=0 else 1
    x=ord(word[i])-op2
    while not FIRST<=x<=LAST:
      x+=ALPHALEN
    ans.append(chr(x))
  return ''.join(reversed(ans))
