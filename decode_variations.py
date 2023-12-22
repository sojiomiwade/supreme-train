'''
            1262
          1 262     
          a bfb
0      1:
1262
x

1 262
a ...


1 26 2
a z  b

12 6 2
l  f b

126 2
x   b

1 2 6 2
a b f b

0:0  1:n
0:1  2:n
0:2  3:n

'' + 1262
'1' + 262
       26 2 

1262
decode(12 62) 
decode(262) 
decode(62) 
decode(2)
decode() -> count = 3
2
62 
count = 0
'''
def decodeVariations(s):
  global count
  def decode(s):
    global count
    if not s:
      count += 1
      return 
    for i in range(len(s)):
      if 1 <= int(s[:i+1]) <= 26:
        decode(s[i+1:])
  count = 0
  decode(s)
  return count
s='1262'
print(decodeVariations(s))def decodeVariations(s):
  def decode(s, i):
    if i == n:
      return 1
    if i in dp:
      return dp[i]
    res = 0
    for k in range(i,n):
      res += int(1<=int(s[i:1+k])<=26) * decode(s, k + 1)
    dp[i]=res
    return res
  dp,n={},len(s)
  
  return decode(s, 0) if s else 0

s='1262'
print(decodeVariations(s)) # 1
s='1'
print(decodeVariations(s)) # 0def decodeVariations(s):
  if not s:
    return 1
  first=0
  if 1<=int(s[0])<=9:
    first=decodeVariations(s[1:])
  second=0
  if 10<=int(s[:2])<=26:
    second=decodeVariations(s[2:])
  return first+second
s='1262'
print(decodeVariations(s)) # 3
s='1'
print(decodeVariations(s)) # 1