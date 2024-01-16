KSI=3
'''
list all sorted strings of length n (alphabetic lowercase)
'''
from typing import List

def issorted(seq) -> bool:
    for ch1,ch2 in zip(seq,seq[1:]):
        if ord(ch1)>ord(ch2):
            return False
    return True

def listsortedperms(n: int) -> List[str]:
    def listsortedperms(idx: int) -> None:
        if idx==n:
            if issorted(buf):
                ans.append(''.join(buf))
            return
        for i in range(KSI):
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

def listsortedperms(n: int) -> List[str]:
    '''
    abc
    ab ba ac ca bc cb


    aaa aab bac
    aa cc ab ba ac ca
    cab acb abc

    duplicates
    ba -> (a) + ba
    aa -> a + (b) + a  

    a b c
    on each bigger iteration, put all the ksi alphabets in the previous results
    '''
    prev_results=['']
    cur_results=[]
    for _ in range(n):
        cur_results=[]
        for pres in prev_results:
            for i in range(KSI):
                res=chr(i+97)+pres
                if issorted(res):
                    cur_results.append(res)
        prev_results=cur_results
    return cur_results

sp=listsortedperms(2)
print(sp)