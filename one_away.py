'''
One Away
if an edit is in (insert, remove, replace) a character a string, given two strings, write a function to check if they're one (or zero) edit away

pale, ple -> true: insert a at 1
pales, pale -> true: insert s at 4
pale, bale -> true: replace p with b
pale, bake -> false: 2 replaces required (two differences found)

don't need delete if we 'start' with smaller string 
cant do insert when strings same length, must resort to replace check
likewise, can't do replace when strings are different, must insert
different len strings must be off by 1


strings have same len
replace check: run, counting number of differences, return imm if a 2nd is found

insert check:
return if len t  - len s != 1 (replace check cheched for 0 already)
s: o r n g e
t: o r a n g e
s: p l e
t: a p l e
s: p l e
t: p l e a  <-- ah ha!

diff spotted? then move j, and rest of s and t must have no diff
no diff spotted, that's ok! it is then 0 or 1 edit away since if t had an extra char, that's only one edit away; and we already chedcked the diff in 2 strings len is 1.



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

#---again
'''
one edit away
pale ple -- true
pales pale -- true
pale bale -- true
pale bake -- false

if s.len == t.len
    is_one_replace_away()
else
    is_one_insert_away()

def is_one_replace_away(s, t)
    count places different.
    return count == 1

s,t:
qple
qpale
^   j
def is_one_insert_away(s, t)
    if t.len < s.len
        s, t = t, s
    assert len.s = len.t - 1

    loop until si not equal tj
    inrement j

    check si = tj till the end (end = is same for both)
'''
def oneaway(s, t):
    if len(s) == len(t):
        return is_one_replace_away(s, t)
    return is_one_insert_away(s, t)

def is_one_insert_away(s, t):
    if len(t) < len(s):
        s, t = t, s
    if len(s) != len(t) - 1:
        return False

    pos = 0
    for k in range(len(s)):
        if s[k] != t[k]:
            pos = k
            break
    else:
        return True #ple and pleq
    n = len(s)
    for k in range(pos, n):
        if s[k] != t[k+1]:
            return False
    return True # no other difference other than at pos found

def is_one_replace_away(s, t):
    count = 0
    for cha, chb in zip(s, t):
        if cha != chb:
            count += 1
    return count <= 1

s, t = 'pale', 'ple' #-- true
print(oneaway(s, t))
s, t = 'pales', 'pale' #-- true
print(oneaway(s, t))
s, t = 'pale', 'bale' #-- true
print(oneaway(s, t))
s, t = 'pale', 'bake' #-- false
print(oneaway(s, t))



'''

johnk
joenm
    i
alreadyfound = True
upon finding another difference, if alreadyfound is true return False
at the end of the string, can just return True

af = true

john
joehn 
--> true

john
jqehn 
--> False
'''
def oneaway(s: str, t: str) -> bool:
    def 
    def same_len_oneaway():
        alreadyfound = False
        for sch, tch in zip(s, t):
            if sch != tch:
                if alreadyfound:
                    return False
                alreadyfound = True
        return True

    return same_len_oneaway() or diff_len_oneaway()