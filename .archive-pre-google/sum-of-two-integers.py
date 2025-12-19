'''
10001 exp 
0010  a
1011  b
0010  c

a 15  01111
b 10  01010

e 25  11001
a 15  10111
b 10  01100
c ..  00100 <- carry places

exp 5 11011 
a -3  11011
b -2  11000
c ..  00000

exp 1 00|0001
a   2 00|0001
b  -1 00|1000
c  .. 00|1000
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a&=((1<<32)-1)
        b&=((1<<32)-1)
        while b:
            c=a&b
            a^=b
            b=(c<<1)&((1<<32)-1)
        # print(a)
        if a&(1<<31)!=0:
            a|=-1<<32
        return a