'''
LLLL RRRR ) (
bal 4 -> 0 -> 1
right= 1
return bal + right

RRRR L
if R comes in and there is bal, remove from bal. otherwise add to right
if L comes in, just add to bal

()( --> 1
bal 1
right 0
'''
def bracket_match(text):
  bal=right=0
  for ch in text:
    if ch=='(':
      bal+=1
    else:
      if bal>0:
        bal-=1
      else:
        right+=1
  return bal+right