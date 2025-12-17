'''
10110100110
1010<-len->
0123

ensure bot is the shorter one
m,n=len(a) and lenght of b

if i is less than n, then take b[i], otherwise take 0 

count the carry, top and bot, 
if the ones are 0 or 2, then append 0. otherwise append 1
if the ones are more than 1, then carry becomes "1". otherwise "0"

0123456789
       012
bar = 6 and lower
=> bar <= 10-3-1

012
11
 1
i
 
m,n 2,1
m-n 1
ans []
carry 0

'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n=len(a),len(b)
        if n>m:
            a,b=b,a
            m,n=n,m
        ans=[]
        carry="0"
        for i in range(m):
            ai=m-i-1
            if ai<m-n:
                bval='0'
            else:
                bi=n-i-1
                bval=b[bi]
            aval=a[ai]
            count=sum(1 for x in (carry,bval,aval) if x=="1")
            if count%2==0:
                ans.append('0')
            else:
                ans.append('1')
            if count>1:
                carry="1"
            else:
                carry="0"
        if carry=="1":
            ans.append('1')
        return ''.join(reversed(ans))