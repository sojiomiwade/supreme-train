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
