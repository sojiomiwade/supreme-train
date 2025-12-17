'''
1 9 9
    9
-----

  1 1 1
9 9 9
9
8 0 0 1
append to ans as long as there is carry or one more element in the inp

carry is involved
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry,ans=1,[]
        for digit in reversed(digits):
            ans.append((digit+carry)%10)
            carry=(digit+carry)//10
        if carry:
            ans.append(1)
        return list(reversed(ans))
        