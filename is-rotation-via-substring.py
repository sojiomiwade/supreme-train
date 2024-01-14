'''
wat|erbottle -- xy
erbottle|wat -- yxyx
substring -- 
'''
def isrotation_via_substr(s1: str, s2: str) -> bool:
    return s1 in 2*s2

s1='waterbottle'
s2='erbottlewat'
print(isrotation_via_substr(s1,s2)) # true
s1='fish'
s2='hsif'
print(isrotation_via_substr(s1,s2)) # false
s1='ooooo'
s2='ooooo'
print(isrotation_via_substr(s1,s2)) # true
s1='waterbotle'
s2='erbottlewat'
print(isrotation_via_substr(s1,s2)) # false

