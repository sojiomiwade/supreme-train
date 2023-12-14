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

'''
carpet cutting
you have a width and a length. how many square carpets can you get. smallest is 1x1
0. 50x17
1. 17x17 --> 17x33
2. 17x33 --> 17x16       2
3. 17x16 --> 1x16        1
4. 1x16                  16
...
19. 1x1 

ans is 12

res = 2 + 1 + 16 = 19
50 // 17 = 2
17//16 = 1
16//1 = 16
w, l = 1, 0

50-34 = 16
1. 16x17
24x5 --> 
24/5=4 count += 4
24%5=4 ==> new carpet dim = 4x5

try 20x5, exp=4
20 5, 15 5, 10 5, 5 5, 1 1 = 5
w=5, l = 0, 
res=20//5 = 4

'''
def cutcount(w: int, l: int) -> int:
    res = 0
    if w < l:
        w, l = l, w
    while w*l != 0:
        res += w//l
        w, l = l, w%l
    return res

print(cutcount(17,50)) # 19