'''
xor both numbers
now use mask to count number of 1s
can apply n&=n-1 to remove a 1 and repeat until n is zero
0100
0011
0000
count 2
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n=x^y
        count=0
        while n:
            count+=1
            n&=n-1
        return count