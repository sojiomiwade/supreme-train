'''
carpet cutting
given dimensions a, and b, return number of squares that can be cut out. smallest square dimension is 1

             a
    --------------------
   |                    |
   |                    | b
   |                    |
    --------------------
a and b : 100 and 3
ans = 100 // 7
then set a to b
b to a % old_b 
repeat this until b equals 0

50 // 25 --> 2
50 % 25 --> 0

'''
def count_squares(a: int, b: int) -> int:
    count=0
    while b!=0:
        count+=a//b
        a,b=b,a%b
    return count

print(count_squares(50,25)) # 2
print(count_squares(50,1)) # 50
print(count_squares(50,23)) # 11
# count 2 5
# 23 50 2
# 4 23  5
# 3 4   1
# 1 3   3
