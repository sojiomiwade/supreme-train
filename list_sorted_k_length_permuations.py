'''
find all k-length strings alphabetically sorted, lower case only

complexity:
time: ck * c**(k-1) * c**2
'''
from typing import List


def ak(lastk: int) -> List[str]:
    def issorted(s: str) -> bool:
        for prev, curr in zip(s, s[1:]):
            if ord(prev) > ord(curr):
                return False
        return True

    alpha_len = 3
    aks = [[None], [chr(i + ord('a')) for i in range(alpha_len)]]
    for k in range(2, lastk + 1):
        res = set()
        for s in aks[k-1]:
            for j in range(len(s)):
                for i in range(alpha_len):
                    ch = chr(i + ord('a'))
                    cand = s[:j] + ch + s[j:]
                    if issorted(cand):
                        res |= {cand}
        aks.append(list(res))
    return aks[-1]

print(ak(3)) #