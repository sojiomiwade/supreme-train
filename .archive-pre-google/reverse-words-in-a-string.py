'''
the sky is blue -- 
[the,sky,is,blue]


eubl si yks the -- reverse the whole thing
blue is sky the -- tokenize by space, then reverse each token
time: O(n), space: O(n) to tokenize the whole thing
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        tokens=s.split()
        return ' '.join(reversed(tokens))