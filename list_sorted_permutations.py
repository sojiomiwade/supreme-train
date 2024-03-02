'''
list all sorted strings of length n (alphabetic lowercase)

3
aaa
aab
aac
caa <--wrong
aca <--also wrong
approach: find all strings of length n and eliminate it if its not 
    sorted

. . . 
for any idx, set all possible values while calling recursively forward for next

'''
from typing import List

'''
alen,n 3 2

buf . . . . 
widx 0
i 0
'''
def list_sorted_permutations(n: int) -> List[str]:
    def issorted(buf: List[str]) -> bool:
        for i in range(n-1):
            if buf[i]>buf[i+1]:
                return False
        return True

    def lsp(widx: int) -> None:
        if widx==n:
            if issorted(buf):
                ans.append(''.join(buf))
        else:
            for i in range(alen):
                buf[widx]=chr(97+i)
                lsp(widx+1)

    alen=3
    buf=['' for _ in range(n)]
    ans=[]
    lsp(0)
    return ans

print(list_sorted_permutations(4))