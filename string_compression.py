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

#16 mins
'''
string compression
length of string: ? 
aabcccccaaa -> a2b1c5a3
count = 1
prev = s0
at the end of each iteration we counted the curr character
for i in range(1,n)
    curr = s[i] #c
    if curr == prev #c == b, no
        count ++
    else 
        res.append(prev + count)
        count = 1
    prev = curr
res.append(prev + count)
'''
from types import resolve_bases


def compression(s: str) -> str:
    if not s:
        return ''
    count = 1
    prev, n, res = s[0], len(s), []
    for i in range(1,n):
        curr = s[i]
        if curr == prev: #c == b, no
            count += 1
        else:
            res.append(str(prev) + str(count))
            count = 1
        prev = curr
    res.append(str(prev) + str(count))
    ress = ''.join(res)
    if len(ress) < n:
        return ress
    return s
s = 'aa'
print(compression(s)) # aa
s = 'a'
print(compression(s)) # a
s = 'aaa'
print(compression(s)) # a3
s = 'aabcccccaaa'
print(compression(s)) # a2b1c5a3


# again, but pre-allocation of exact amount of buffer needed!
'''
compress a string
think of the time & space complexity
aaaaabccc
a5b1c3
allocation. how? pass through once and figure it out
count = 1
for each char if not eq to previous, 
    count ++
count ++
buflen = 2*(count)

avoid the 2 passes?

aaaaabccc
a5b1c3
'''
def compress(s: str) -> str:
    if not s:
        return s
    count = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            count += 1
    count += 1
    buflen = 2 * count
    clis = ['' for _ in range(buflen)]
    print('clis len', buflen)

    clis_idx = 0
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            clis[clis_idx] = s[i-1]
            clis[clis_idx+1] = str(count)
            clis_idx += 2
            count = 0
        count += 1
    clis[clis_idx] = s[-1]
    clis[clis_idx+1] = str(count)
    return ''.join(clis)

s = 'aaaaabccc'
print(compress(s)) # 6, a5b1c3
s = 'aa'
print(compress(s)) # 2, a2


'''
string compression
implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. if the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z)
aabcccccaaa
l r
a2b1c5a3
can make new string and write the compressed string there: O(n), O(n)
can alter the current string too, without this extra space in place: O(n), O(1), then trim it? NO, it seems

ba
a1
b1
writing from either side will destroy original string! in a way we can't continue
so have to make a copy!
make a pass to know whether to even bother. then do it. can use a vector to track frequencies
    then loop over that vector specifying char and count to make the new list of strings easily if 2*the vec length is less than original_string's length
ab
'''
def compress(string: str) -> str:
    count = 1
    buffer = []
    for idx in range(1, len(string)):
        if string[idx] != string[idx-1]:
            count += 1
    if 2 * count >= len(string):
        return string
    '''
    aabcccccaaa
    0123

    run through with i
    count += 
    '''
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1 # 2
        else:
            buffer.append(string[i-1]+str(count))
            count = 1
    buffer.append(string[-1]+str(count))
    return ''.join(buffer)

string = 'ab'
print(compress(string)) #ab
string = 'aabb'
print(compress(string)) #aabb
string = 'aabbb' 
#           ^
print(compress(string)) #a2b3