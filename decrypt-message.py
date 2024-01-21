'''
100    26
ascii: 97 - 123

Step 2:	100	214	319	428	529

Step 1:	99	114	105	109	101
Step 3:	100	110	111	116	113

113 - 116 = -3
-3 + 26
ans for that row
go to the next one and do the same

so first pass awesome!!!!! i did it!@!!!!Q YESSS

get residue (from the back)
'''
def decrypt(word):
  n=len(word)
  res=[0 for _ in range(n)]
  for i in range(n-1,-1,-1):
    res[i]=ord(word[i])-(ord(word[i-1]) if i>0 else 1)
    while not 97<=res[i]<=123:
      res[i]+=26
  return ''.join([chr(num) for num in res])

word='dnotq' #expect crime
print(decrypt(word))