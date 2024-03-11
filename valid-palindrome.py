'''
come from the left and right
valid left/right is alphanum
a man, a plan, a canal: panama
l
                              r
return false anytime ch of l and r are not the same
once l and r cross, return true

97 --> 

a,a
  l
 r
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        left,right=0,n-1
        while left<=right:
            while left<=right:
                ch=ord(s[left])
                if ord('0')<=ch<=ord('9') or ord('a')<=ch<=ord('z') or ord('A')<=ch<=ord('Z'):
                  break
                left+=1
            while left<=right:
                ch=ord(s[right])
                if ord('0')<=ch<=ord('9') or ord('a')<=ch<=ord('z') or ord('A')<=ch<=ord('Z'):
                  break
                right-=1
            if left>right or s[left].lower()==s[right].lower():
                left+=1
                right-=1
            else:
                return False
        return True


