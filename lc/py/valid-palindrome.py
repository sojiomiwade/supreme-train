# a jfdkj;l;fsd;;;
# i
#                j
# i moves until next alphanum
# j does the same other direction
# if they have not hit the same char
#     compare for palindronme --> false if not the same
# return true if they are at same char
# ;;aa
#    i  
#   j
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i,j = 0, n-1
        while i<j :
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i,j = i+1, j-1
        return True # won't happen