'''
     b
   --------
a |
  |     |
   --------
time: 11:55 - 12:11 = 16 mins
given dimensions a, and b, return number of squares that can be cut out. smallest square dimension is 1
biggest square has dim min(a,b), so next remaining to consider is
max(b,a)-min(b,a) and min(a,b). 
no need for recursion
'''
def min_squares(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError(a, b)
    count = 1
    while a > 1 or b > 1: # 1,1
        print(a,b)
        a, b = (max(b,a)-min(b,a), min(a,b))
        count += 1 # 1
    return count


print(min_squares(2, 1)) # 2
print(min_squares(2, 3)) # 3
print(min_squares(0, 1)) # error

