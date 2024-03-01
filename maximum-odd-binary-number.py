'''
count the 1s --> count
remove 1 (for the right)
put the rem in front
n-count
(count-1)*1 + (n-count)*0 + 1
'''
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        count=sum(1 for x in s if x=='1')
        return (count-1)*'1'+(n-count)*'0'+'1'