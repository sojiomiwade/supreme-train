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
print(decodeVariations(s))