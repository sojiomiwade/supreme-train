'''
1010
1011

0101
110


tval,bval,cval
come from the back, and always get a val!
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cval=0
        m,n=len(a),len(b)
        maxmn=max(m,n)
        ans=[]
        for i in range(maxmn):
            aval=0
            if m-1-i>=0:
                aval=int(a[m-1-i])
            bval=0
            if n-1-i>=0:
                bval=int(b[n-1-i])
            valsum=cval+aval+bval
            ans.append(str(valsum%2))
            cval=valsum//2
            
        finalans='1' if cval else '' 
        finalans+=''.join(reversed(ans))
        return finalans