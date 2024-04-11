'''
One Away
if an edit is in (insert, remove, replace) a character a string, given two strings, write a function to check if they're one (or zero) edit away

pale ale true
pale kale true
pale kele false -- 2 edits
pale ali false -- 2 edits


consider s is the bigger string, and ignore insert

p a l e
  i
j
a l e

eq
i
j
e
found 0
abcde
    i
   j
abde
found 1

when there is a difference, advance only on s, and set difffound to true. if another is found, return false.
'''
def one_del_away(s: str, t: str) -> bool:
    i=j=0
    m,n=len(s),len(t)
    assert m!=n
    if m<n:
        s,t=t,s
        m,n=len(s),len(t)
    if m-n!=1:
        return False
    diff_already_found=False
    while i<m and j<n:
        if s[i]!=t[j]:
            if diff_already_found:
                return False
            diff_already_found=True
            i+=1
        else:
            i,j=i+1,j+1
    return True

s,t='abcde','abde'
print(one_del_away(s,t)) # true
s,t='pale','ale'
print(one_del_away(s,t)) # true
s,t='ale','alep'
print(one_del_away(s,t)) # true
s,t='abcde','abd'
print(one_del_away(s,t)) # false
s,t='pale',''
print(one_del_away(s,t)) # false
s,t='ale','qlep'
print(one_del_away(s,t)) # false


