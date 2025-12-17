'''

4 5 6 7 8 9 10 <-- above + 7
5 6 7 8
1 2 3 4
to the sum, add m*x

1 
m weeks (7(7+1)/2)*m + (m-1)*7
x days:  x(x+1)/2 + x 

day 10
10 div 7 for the number of weeks -- 1 here
10 mod 7 for the extra days -- 3 here 

28 + (6+3)

m t w r f s u
1 2 3 4
m,x 0,4

m t w r f s u
1 2 3 4 5 6 7
2 3 4 5 6 7 8 <--  7
3 4 5 6 7 8 9 <--  2*7
               --  3*7
7*(7+1)//2*3 + 14
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        m,x=n//7,n%7
        weeks=7*(7+1)//2*m + sum(7*w for w in range(1,m))
        extra=x*(x+1)//2+(m*x)
        print(m,x,weeks,extra)
        return weeks+extra
