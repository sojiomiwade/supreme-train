'''
abab

0123456
aababba
l  r
add mf to rem=k to get r-l+1

aabqra
--kk
as long as rem<=k, we are good
and rem = r-l+1 - mf

ABAXYZ
-------
l     
   k
     r
r can increase as long as r-l+1-mf<=k
slide l with r if there is a violation
 0-----7

 10-6<=4
 10-1<=4
 10-8<=4
 no need to use max of count.values, 
 
 a b a b | k 1 | exp 4
   l
       r
count {a2 b1}
mf 2 
2>2
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=Counter()
        left,n=0,len(s)
        mf=-1
        for right in range(n):
            count[s[right]]+=1
            mf=max(mf,count[s[right]])
            if right-left+1-mf>k:
                count[s[left]]-=1
                left+=1
        return n-left

            