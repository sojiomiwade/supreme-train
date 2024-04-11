'''
X can say if something comes after me and it is bigger, then remove X from sum
Likewise I, and C
now this way, you either add the token or remove it. simple!
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        letters='IVXLCDM'
        values=[1,5,10,50,100,500,1000]
        vl={let:val for let,val in zip(letters,values)}
        ans=0
        n=len(s)
        for i in range(n):
            if i+1<n and vl[s[i]]<vl[s[i+1]]:
                ans-=vl[s[i]]
            else:
                ans+=vl[s[i]]
        return ans

