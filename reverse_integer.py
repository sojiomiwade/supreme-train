'''
assume shouldn't convert it to string...
first: use modulo and div to get each digit from the right, while making a new number with those. 


checking for overflow:
suppose 12343 was INT_MAX
in general cannot check x*10>INT_MAX

ex if x=1235, can't check 1235*10>INT_MAX
so check 1235>INT_MAX//10

but if x and INT_MAX//10 are equal, need more checking
check 1234*10==INT_MAX and 3>INT_MAX%10
for negative numbers, last digit is one more so use INT_MAX+(is_odd)

54321
1234
'''
class Solution:
    def reverse(self, x: int) -> int:
        y=0
        isneg,x=x<0,abs(x)
        INTMAX=2**31-1
        LID=INTMAX%10
        while x:
            dig=x%10
            if y>INTMAX//10 or (y==INTMAX//10 and dig>LID+isneg):
                return 0
            y*=10
            y+=dig
            x//=10
        return -y if isneg else y