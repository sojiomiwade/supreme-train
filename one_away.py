'''
One Away
insert, remove, edit to get the same
if len of s and t are same, can only use edit
else, can use insert (ignore remove since we can always start with smaller string)
func edithelps -> boolean: 
    assert len of s and t are same
    verify only one loc is different
    return true/false accordingly
func inserthelps -> boolean
    if len of s > len of t, then swap them
    assert len of s is exactly one less than t
        pale ... ple 
        ple ... pale
    verify one insert helps
        find first char where there's a difference
        verify the rest of the strings are the same
t and s:
p a l e
p l e
  ^
p a l e
p q e

abc
ac
^
first = 1
sidx moves by one, but don't move tidx
then verify rest of string
pale
fish
'''

def one_away(s: str, t: str) -> bool:
    def edithelps() -> bool:
        print("via edit: ", end='')
        return sum(1 if ch_s != ch_t else 0 for ch_s, ch_t in zip(s, t)) <= 1
        
    def inserthelps() -> bool:
        nonlocal s, t
        print("via insert/remove: ", end='')
        if len(s) > len(t):
            s, t = t, s
        if len(t) - len(s) != 1:
            return False
        for idx in range(len(s)): 
            if s[idx] != t[idx]:
                startidx = idx     #startidx = 1
                break
        else:
            return True
        for idx in range(startidx, len(s)):
            if s[idx] != t[idx + 1]:
                return False
        else:
            return True

    if len(s) == len(t):
        return edithelps()
    return inserthelps()

s, t = 'aaa', 'bb'
print(one_away(s, t)) # False, via insert
s, t = 'pale', 'bale'
print(one_away(s, t)) # true, edit
s, t = 'pale', 'ale'
print(one_away(s, t)) # true, insert
s, t = '', ''
print(one_away(s, t)) # true, edit
s, t = 'a', ''
print(one_away(s, t)) # true, insert
s, t = 'ab', ''
print(one_away(s, t)) # true, insert

