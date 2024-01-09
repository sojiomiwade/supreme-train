'''
))) ((()()))
'''
def bracket_match(text):
  uright = 0
  left = 0
  for bracket in text:
    if bracket == ')':
      if left == 0:
        uright += 1
      else:
        left -= 1
    else:
      left += 1
  return uright + left

print(bracket_match(')))')) # 3
print(bracket_match('((()))')) # 0
print(bracket_match(')))((((')) # 7

