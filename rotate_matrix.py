'''
problem: rotate n x n matrix
1 2 3       7 4 1
4 5 6 -->   8 5 2
7 8 9       9 6 3
--
20 00
10 01
00 02

a b c d     m i e a
e f g h     n j f b
i j k l     p k g c
m n p q     q l h d

approach: 
res = [n][n]
for j = 0 to n-1:
    for i = n-1 to 0
        res[j][n-1-i] = mat[i][j]
approach 2
right: a[count][count:n-count], +1
down:  a[count:n-count][n-1-count], +1
left:  a[n-1-count][n-1-count:-1+count], -1
up:    a[n-1-count:-1+count][count], -1

d = dict(
        right=(count,range(count:n-count), 1),
        right=(count:n-count
for count in 0 to n - 1:
    for 

 or down

isrow = True # take a row and write onto a column
temp = int[n]
dir = 0
for count in 0 to n - 1:
    for dir in (right, down, left, up)
        if dir in right down
            for i in range(n - count)
                temp[i] = mat[i][n - 1 - count]
        else
            for j in range(n - count)
                temp[j] = mat[n - 1 - count][j]
        if dir == 1
            else dir = 0
        else
            dir = 1
        isrow = not isrow


    temp = copy of mat[count][count:n-count]
    if 
        for i in range(n - count):
            mat[]
    else
        for j in range(n - count):
            mat[]
clarify: 
    to the right or left? 
time: O(n^2)
space: O(n^2)



'''
from typing import List


def rotate(mat: List[List[int]]) -> List[List[int]]:
    n = len(mat)
    res = [[0 for j in range(n)] for i in range(n)]
    for j in range(n):
        for i in range(n-1,-1,-1):
            res[j][n-1-i] = mat[i][j]
    return res

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(rotate(mat))

