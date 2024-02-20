'''
Rules:

1. The first line cannot be indented
2. Control statements end with a colon (:)
3. Control statements must be followed by a line that is indented at least one more space than the control statement itself
4. Lines after non-control statements must have an indent equal to the previous line or some valid enclosing block

Assumptions:

- There are no trailing spaces
- No blank or null lines
- No special characters

print("begin")
if s == "dance":
 for i in range(0, 10):
      print()
      if i % 3 == 0:
            print("beguine")
      else:
        print("rumba")
      valid  
   invalid
  invalid
 valid     
  ||||||print("dumba")
    print("stop the music") <-- any indent above can decide the validity

0 1 5 3 <-- wrong because it finds no three
    if i
control indents go on stack
invalid when 

validate 1st line is not indented
for any line, 
    if prior was control, 
        verify i am indented inside control
        place my indent on stack
    else
        repeatedly remove any indent that is more from stack
        if top of stack is not equal to you, return False
        then place this line on stack (perhaps on equal indents)
return True
'''
from typing import List

def first(s: str) -> int:
    for idx,ch in enumerate(s):
        if ch!=' ':
            return idx
    raise Exception('empty line')

'''
print("begin")
if s == "dance":
 for i in range(0, 10):
      print()
      if i % 3 == 0:
            print("beguine")
      else:
        print("rumba")
        print("dumba")
prev,cur:
      else:
        print("rumba")
'''
def isvalid(s: str) -> bool:
    lines=s.split('\n')
    if first(lines[0])>0:
        return False
    st=[0]
    for idx in range(1,len(lines)):
        prev,cur=lines[idx-1],lines[idx]
        if prev[-1]==':':
            if first(cur)<=first(prev):
                return False
            st.append(first(cur))
        else:
            while st[-1]>first(cur):
                assert st
                st.pop()
            assert st
            if st[-1]!=first(cur):
                return False
            st.append(first(cur))
    return True
s='''
print("begin")
if s == "dance":
 for i in range(0, 10):
      print()
      if i % 3 == 0:
            print("beguine")
      else:
        print("rumba")
        print("dumba")
'''
print(isvalid(s[1:-1])) # true

s='''
print("begin")
if s == "dance":
 for i in range(0, 10):
      print()
      if i % 3 == 0:
            print("beguine")
      else:
        print("rumba")
        print("dumba")
    print()
'''
print(isvalid(s[1:-1])) # false

s='''
print("begin")
if s == "dance":
 for i in range(0, 10):
      print()
      if i % 3 == 0:
            print("beguine")
      else:
        print("rumba")
        print("dumba")
 print()
'''
print(isvalid(s[1:-1])) # true