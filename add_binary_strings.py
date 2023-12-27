'''

1011010 -- 7
   1011 -- 4

aval, bval, carry
res=a[:n-m]
zip out tuple from the reverse and do the carry thing!
 11
  1
 --
100

0
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n,m=len(a),len(b)
        if n<m:
            a,b=b,a
            n,m=m,n
        carry=0
        res=[]
        
        for ach,bch in zip(reversed(a),reversed('0'*(n-m)+b)):
            aval,bval=int(ach),int(bch)
            res.append(str((aval+bval+carry)%2))
            carry=(aval+bval+carry)//2
        return ('1' if carry else '') + ''.join(reversed(res))
        