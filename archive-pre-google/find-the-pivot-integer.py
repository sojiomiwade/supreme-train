'''
1 2 3 4 5 6 7 8
right 5 6 7 8
left 1 2 3 4 5

4
0 1 2 3 4
for i in 1 to n 
    add i, to left, return i if sum is the same
    remove i from right

right

1 2 3
    x
left 6
right 3
ans should be 2
'''
class Solution:
    def pivotInteger(self, n: int) -> int:
        left=0
        right=sum(i for i in range(n+1))
        for x in range(1,n+1):
            left+=x
            if left==right:
                return x
            right-=x
        return -1