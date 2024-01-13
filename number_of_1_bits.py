'''
11101
11100
11000      11011
1
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        #2nd:
        #if n>0 incremnt count; use n&(n-1)to drop the lowest bit, 
        ans=0
        while n:
            ans+=1
            n&=n-1
        return ans
        #first:
        # mask=1
        # ans=0
        # for _ in range(32):
        #     ans+=(n&mask)!=0
        #     mask<<=1
        # return ans
