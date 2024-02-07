'''
isvalid()
Rules: 

1. The first line cannot be indented
2. Control statements end with a colon (:)
3. Control statements must be followed by a line that is indented at least one more space than the control statement itself
4. Lines after non-control statements must have an indent equal to the previous line or some valid enclosing block

Assumptions:

- There are no trailing spaces 
- No blank or null lines
- No special characters
'''

from typing import List,Tuple


def indent(line: str) -> int:
    for i in range(len(line)):
        if line[i]!=' ':
            return i
    raise ValueError(f'every line must have a nonspace char')

def isvalid(lines: List[str]) -> Tuple[List[int],bool]:
    # print("begin")              <
    # if s == "dance":
    #  for i in range(0, 10):     <
    #       print()               <
    #       if i % 3 == 0:
    #             print("beguine")    <
    #       else:
    #         print("rumba")          <
    #         print("dumba")
    #     print("stop the music")
    # st=[0,2]
    # prevline_was_control,prev_indent=false,0
    # cur_is_control,cur_indent=N,0
    if indent(lines[0])>0:
        return [],False
    st=[]
    prevline_was_control=None
    prev_indent=None
    for line in lines:
        cur_is_control=line[-1]==':'
        cur_indent=indent(line)
        if prevline_was_control:
            assert prev_indent is not None
            if cur_indent <= prev_indent:
                return st,False
            elif cur_is_control:
                st.append(cur_indent)
        else:
            while st and st[-1]>=cur_indent:
                st.pop()
            if cur_is_control:
                st.append(cur_indent)
        prevline_was_control = cur_is_control
        prev_indent=cur_indent
    return st,True

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
    print("stop the music")
'''
lines=s.split('\n')
print(isvalid(lines[1:len(lines)-1])) #True


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
    print("stop the music")
        a
          b
        c
          d
'''
lines=s.split('\n')
print(isvalid(lines[1:len(lines)-1])) #True

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
    print("stop the music")
        a
          b
        c
          d
'''
lines=s.split('\n')
print(isvalid(lines[1:len(lines)-1])) #true


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
    print("stop the music")
        a
          b
        c
          d
'''
lines=s.split('\n')
print(isvalid(lines[1:len(lines)-1])) #false


