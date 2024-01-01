'''
find all k-length strings alphabetically sorted, lower case only

aaaa
aaab
aaac
   ^
at each idx, pass 
each child idx, can only do parent idx or greater   
i.e., parent passes the start idx
'''
from typing import List


def ak(k: int) -> List[str]:
    def ak(cur_buf_idx: int, start_ascii_idx: int) -> None:
        if cur_buf_idx==k:
            res.append(''.join(buf))
        else:
            for i in range(start_ascii_idx,MAX_ASCII_IDX):
                buf[cur_buf_idx]=chr(ord('a')+i)
                ak(cur_buf_idx+1,i)
    buf=['' for _ in range(k)]
    MAX_ASCII_IDX=26
    res=[]
    ak(0,0)
    return res

ans=ak(3)
assert len(ans)==len(set(ans))
for s in ans:
    for cha,chb in zip(s,s[1:]):
        assert ord(cha)<=ord(chb)
#print(ans) # [aaa,aab,...,aaz,...,zzz]
for x in ans:
    print(x)
print(len(ans))