'''
hello world
     i
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        def lastword():
            i=n-1
            while s[i]==' ':
                i-=1
            ans=[]
            while i>=0 and s[i]!=' ':
                ans.append(s[i])
                i-=1
            return ''.join(ans)

        n=len(s)
        return len(lastword())