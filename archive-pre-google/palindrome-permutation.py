'''
given a string, find if it is a permutation of a palindrome. assume ascii

hhhha
first: hashmap counter every key should have even count; one can have odd count. time is n
2nd: could use 256 bit vector. then at the end only one key can have a set bit. time still n, space O(256). ignore the space
3rd: sort it and count neighbors. come back here since it's n lg n to start

ahhhh
f t t     t
0 1 2 ... 8 ...
ube=t
'''
def ispalperm(s: str) -> bool:
    isbal=[True for _ in range(256)]
    for x in s:
        isbal[ord(x)]=not isbal[ord(x)]
    unbalanced_exists=False
    for x in s:
        if not isbal[ord(x)]:
            if unbalanced_exists:
                return False
            unbalanced_exists=True
    return True

print(ispalperm('ahhhh')) # t
print(ispalperm('ahhh')) # f
print(ispalperm('noon')) # t
print(ispalperm('noon1122')) # t
print(ispalperm('noon11223')) # t
print(ispalperm('noon112234')) # f