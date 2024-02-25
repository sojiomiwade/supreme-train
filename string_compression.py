'''
string compression
implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. if the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z)
aabcccccaaa
          i
a2b1c5a3
could use a new string. 
with one pass can know whether to bother. and also how much space to preallocate: (1+number of differences) times 2
if that many is greater than string length, don't bother

count starts at 1, 
clear buf when difference is seen
at the end, we still need to add the last count
abbc
aaaaabcccccaaa
     i

s: a b b b b b c
                 j
m,n 6,7
ans a 1 b 5 . . 
            i
count 1 
'''
def compress(s: str) -> str:
    n=len(s)
    count=0
    for i in range(1,n):
        if s[i]!=s[i-1]:
            count+=1
    m=(1+count)*2
    if m>=n:
        return s
    ans=['' for _ in range(m)]
    j=1
    for i in range(0,m,2):
        count=1
        while j<n and s[j]==s[j-1]:
            count+=1
            j+=1
        ans[i:i+2]=[s[j-1],str(count)]
        j+=1
    return ''.join(ans)

s='aabcccccaaa'
print(compress(s))
s='aabccccca'
print(compress(s))
s='abca'
print(compress(s))


