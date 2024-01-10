'''
string compression
implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. if the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z)

a a b c c c c c a a a

first approach: on new letter: put the old one down with count, reset the count
2nd if input is string buffer: hmm we could overwrite, especially if output is longer than input

'''
def compress(s: str) -> str:
    if not s:
        return ''
    ans=[]
    count=1
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            ans.extend([f'{s[i-1]}{count}'])
            count=1
        else:
            count+=1
    ans.extend([f'{s[-1]}{count}'])
    t=''.join(ans)
    return t if len(t)<len(s) else s

print(compress('aabcccccaaa')) #a2b1c5a3
print(compress('aabcccccaaQ')) #a2b1c5a3Q1
print(compress('abcde')) #abcde