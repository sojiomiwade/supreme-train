'''
more than 26 => false
first: hashset: if you see something already there return false. at the end, return true. t,s: n,n
alt: sort and check neighbors. t,s: n lg n, n in general but can be O(1). really just n since it's a str, not a str buffer
'''
def isunique(s: str) -> bool:
    t=sorted(s)
    n=len(s)
    for i in range(1,n):
        if t[i]==t[i-1]:
            return False
    return True

print(isunique('something'))
print(isunique('isunique'))
print(isunique('print'))
print(isunique('Aba')) #true
print(isunique('#$#$!#')) #false
print(isunique('!@#$%')) #true
