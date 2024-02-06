'''given dimensions a, and b, return number of squares that can be cut out. smallest square dimension is 1


 ______________a________
|                      |
|                      |b
|______________________|

a x b
a//b square carpets
then set a,b to b,a%b
repeat until a,b=1,1

10
3
10,3 -> 3
3,1 -> 3
1,0-> 
break when b==0

1,1 -> 1
1,0 -> break
'''
def count_squares(a: int, b: int) -> int:
    assert a and b
    if b>a:
        a,b=b,a
    ans=0
    while b:
        ans+=a//b
        a,b=b,a%b
    return ans

a,b=10,3
print(count_squares(a,b)) # 6

a,b=9,3
print(count_squares(a,b)) # 3

a,b=12,5
'''
12,5 -> 2
5,2 -> 2
2,1 -> 2
1,0 -> break
'''
print(count_squares(a,b)) # 6
