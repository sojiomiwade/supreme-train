'''
List all k-length permutations that are sorted (lowercase only)
k=3
abd
abc
aaa
no! --> bba
-----
0.. k

k=2
aux [aa]
printed: aa,ab,ac,ad,ae
'''
from typing import List


def list_sorted_k_perm(k: int) -> None:
    def sorted(arr: List[str]) -> bool:
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                return False
        return True

    def listsorted(aux: List[str]):
        if len(aux)==k:
            if sorted(aux):
                print(''.join(aux))
        else:
            for i in range(3):
                listsorted(aux+[chr(ord_a+i)])

    ord_a=ord('a')
    listsorted([])

list_sorted_k_perm(3)
# list_sorted_k_perm(4)