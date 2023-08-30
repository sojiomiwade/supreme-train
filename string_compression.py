'''
string compression
length of string: ? 
0 possible. just return empty 
ELSE: 
aabcccccaaa
^
while more chars in s
    compress the next substring

count = 1
ch-i-1 = s[0]
for ch in s[1...n]
    if ch-i != ch-i-1
        t.append(ch-i-1 + count)
        count = 1
    else 
        count ++
t.append(ch(len(s)-1 + count)
time: O(n)
space: O(1) and return val is O(n)
a2bc5a3

'''
def compressed(s: str) -> str:
    tarr = []
    count = 1
    prev = s[0] # a
    for i in range(1, len(s)): # a...
        prev, curr = s[i-1], s[i]
        if prev != curr:
            tarr.append(prev + str(count))
            count = 1
        else:
            count += 1
    tarr.append(s[-1] + str(count))
    t = ''.join(tarr)
    return t if len(t) < len(s) else s

s = 'aabcccccaaa'
print(compressed(s)) # a2b1c5a3
s = 'aa'
print(compressed(s)) # aa
s = 'aaa'
print(compressed(s)) # a3

#time to finish: 20 mins
