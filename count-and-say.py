'''
cs(21) = one 2 one 1 = 12 11
cs(n) = express(cs(n-1))
e(3322233333)
freq+val + freq+val + ...
223
  i
count 1
ans [22 13]
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        def express(s: str) -> str:
            i,n=0,len(s)
            ans=[]
            while i<n:
                count=1
                while i+1<n and s[i]==s[i+1]:
                    count+=1
                    i+=1
                ans.append(f'{count}{s[i]}')
                i+=1
            return ''.join(ans)

        ans=prev='1'
        for _ in range(n-1):
            ans=express(prev)
            prev=ans
        return ans