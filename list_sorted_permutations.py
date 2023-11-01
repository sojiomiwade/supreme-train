'''
list all strings of length k, having letters a - e only that are sorted
k=3
abc
aaa
cab <--no

each recursive call: 
base case: if string is k in length, we are done
loop through a - e, add that to prefix.

a -> a
'''
from typing import List


def list_sorted(k: int) -> None:
    def helper(prefix: List[str]) -> None:
        if len(prefix) == k:
            for i in range(1,len(prefix)):
                if ord(prefix[i-1]) > ord(prefix[i]):
                    break
            else:
                print(''.join(prefix))
            return
        for i in range(5):
            ch = chr(97+i)
            prefix.append(ch)
            helper(prefix)
            prefix.pop()
    helper([])

list_sorted(2) # a, b, c,d,e
'''
print all strings of length k where the characters are in sorted order.

generate each string of length k, then check if it is sorted
'''
def print_sorted_strings(k: int) -> None:
    '''
    aaaa
    aaab
    prefix method
    abcd,
        bcd,a

        acd,b
        abc,d
    
    4,.
        3,a
           2,aa 
        3,b
            2,ba
            2,bb
        3,c
        ...
    '''
    def _sorted(s: str) -> bool:
        for i in range(1, len(s)-1):
            if ord(s[i-1]) > ord(s[i]):
                return False
            return True

    def _print_sorted_strings(rem: int, prefix: str) -> None:
        if rem == 0:
            if _sorted(prefix):
                print(prefix)
            return
        for i in range(26):
            _print_sorted_strings(rem - 1, prefix + chr(i+ord('a')))
    _print_sorted_strings(k, '')

print_sorted_strings(5) #aaaa, aaab, ...