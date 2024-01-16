'''
list all sorted strings of length n (alphabetic lowercase)
'''
from typing import List

def issorted(lis: List[str]) -> bool:
    for ch1,ch2 in zip(lis,lis[1:]):
        if ord(ch1)>ord(ch2):
            return False
    return True

def listsortedperms(n: int) -> List[str]:
    def listsortedperms(idx: int) -> None:
        if idx==n:
            if issorted(buf):
                ans.append(''.join(buf))
            return
        for i in range(26):
            buf[idx]=chr(97+i)
            listsortedperms(idx+1)
    '''
    T(n)=ksi * T(n-1) -> n * (ksi)!
    3
    use buf to build out each perm with DFS approach; at end filter out unsorted
    later, can build into sol always starting next char from the prev one
    '''
    buf=['' for _ in range(n)]
    ans=[]
    listsortedperms(0)
    return ans

sp=listsortedperms(3)
print(sp)