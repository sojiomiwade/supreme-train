'''
       26
a-z -> 97-123
A-Z -> 65-91
65+?=97->32
abc
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def lower(ch: str) -> str:
            ordch=ord(ch)
            assert isalphanum(ch)
            if ORD_HIGHER_A<=ordch<=ORD_HIGHER_Z:
                return chr(ordch+SEP)
            return ch

        def isalphanum(ch: str) -> bool:
            ordch=ord(ch)
            if ord('0')<=ordch<=ord('9'):
                return True
            if ORD_HIGHER_A<=ordch<=ORD_HIGHER_Z or ORD_LOWER_A<=ordch<=ORD_LOWER_Z:
                return True
            return False

        SEP=32
        ORD_LOWER_A,ORD_LOWER_Z,ORD_HIGHER_A,ORD_HIGHER_Z=(
            97,97+25,65,65+25
        )
        left,right=0,len(s)-1
        while left<right:
            while left<right and not isalphanum(s[left]):
                left+=1
            while left<right and not isalphanum(s[right]):
                right-=1
            if left>=right:
                return True
            sleft=lower(s[left])
            sright=lower(s[right])
            if sleft!=sright:
                print(f'{(left,right)}:{(sleft,sright)}:{(s[left],s[right])}')
                return False
            left+=1
            right-=1
        return True