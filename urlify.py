'''
in-place replace all spaces with '%20'
 0123
'fish   '
'fish   '

    x
01234
    
'''
from typing import List
def urlify(s: List[str], olen: int) -> None:
    srep='%20'
    width_srep=len(srep)
    scount=sum(1 for i in range(olen) if s[i]==' ')
    nlen=(width_srep-1)*scount + olen
    j=nlen-1
    for i in range(olen-1,-1,-1):
        ch=s[i]
        if ch==' ':
            s[j-2:j+1]='%20'
            j-=width_srep
        else:
            s[j]=ch
            j-=1

ostring='Mr John Smith'
s=list(ostring+''.join(str(i) for i in range(10)))
print(f"{''.join(s)}")
urlify(s,len(ostring))
print(f"{''.join(s)}") #oldstring + 456789