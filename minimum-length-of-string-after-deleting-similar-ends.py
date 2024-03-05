'''
c abaaba c
aabccabba
  l
        r
while left is less than right and left and right char are the same
    loop on left forward until cur is different from prev
    likewise on right going leftwards
return right-left+1

cabc
 l
  r
prev c

cc
  l
 r
cac
 l
 r
'''
class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        left,right=0,n-1
        while left<right and s[left]==s[right]:
            prev=None
            while left<=right and (not prev or s[left]==prev):
                prev=s[left]
                left+=1
            prev=None
            while left<=right and (not prev or s[right]==prev):
                prev=s[right]
                right-=1
        return right-left+1
