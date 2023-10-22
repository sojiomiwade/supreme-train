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


#begin in place approach
'''
zero matrix
write an algorithm such that if matrix[i][j] == 0, then ensure
1. matrix[i][k] = 0, for all k 
2. matrix[k][i] = 0, for all k



rotate matrix 

1 2 3
4 5 6
a b c

a 4 1
b 5 2
c 6 3

res = same size as matrix
for c in range(n):
    for r in range(n-1,-1,-1): r in [2,0]
        res[c][n-1-r] = matrix[r][c]
print(res)
complexity: O(n**2), O(n**2)

inplace:
do this for each layer (n layers)
    temp = top          O(n)
    top = left          O(n)
    left = bottom       n
    bottom = right      n
    right = top         n
O(n**2),O(n)
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
n = len(matrix)


right = 

'''
res = [[0 for _ in range(n)] for _ in range(n)]
for c in range(n):
    for r in range(n-1,-1,-1): #r in [2,0]
        res[c][n-1-r] = matrix[r][c]
'''
print(matrix)

#--bah below wont work as it assumes the columns wont write on each other
'''
a b c d
e f g h
i j k l
m n o p

m i e a q r # n = 6
n j f b . . 
o k g c . . 
p l h d . . 

any of n rows do: col i -> row j
use temp to rotate_layer: 
    temp = top
    top = left
    left = bottom
    bottom = right
    right = top

for layer in [:n]
    repeat rotate_layer(layer)
'''
from typing import List
def rotate_matrix(matrix: List[List[int]]) -> None:
    '''
    0 1
    2 3
    ---
    2 1
    3 3
    temp = 01
    m00=m10=2
    m10=3
    '''
    def rotate_layer() -> None:
        temp = [matrix[layer][k] for k in range(layer,n-layer)]
        for k in range(layer,n-layer-1): #[0:1]
            matrix[layer][k] = matrix[n-1-k][layer] #top=left: 00=10,01=10
        for k in range(layer,n-layer-1):
            matrix[n-1-k][layer] = matrix[n-1-layer][n-1-k] # left=bottom
        for k in range(layer,n-layer-1):
            matrix[n-1-layer][n-1-k] = matrix[k][n-1-layer] # bottom=right 
        for k in range(layer,n-layer-1):
            matrix[k][n-1-layer] = temp[k-layer] # right = 

    n = len(matrix)
    for row in matrix:
        print(row)
    print()
    for layer in range(n//2):
        rotate_layer()
    for row in matrix:
        print(row)

dim = 4
matrix = [[0 for _ in range(dim)] for _ in range(dim)]
for i in range(dim):
    for j in range(dim):
        matrix[i][j] = dim*i + j
rotate_matrix(matrix)

# rotate matrix in place with 2 for loops
'''
rotate a matrix in-place to the right
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

1 4 7
- - 
7 8 9
temp = top
top = left
left = bottom
bottom = right
right = temp

layer
for layer in range(len(matrix) // 2)
    for i in range(n):
        temp[i] = matrix[0][n-1-i]
    for i in range(n) # left to top
        matrix[0][n-1-i] = matrix[i][0]
    for i in range(n) # bottom to left
        matrix[i][0] = matrix[n-1][i]
    for i in range(n) right to bottom
        matrix[n-1][i] = matrix[n-1-i][n-1]
    for i in range(n)
        matrix[n-1-i][n-1] = temp[i]
don't write last element for any, because that is just duplicating
first of new. instead see that  
actually doesn't matter, instead start from the intersecting corner
'''
from typing import List

def print_matrix(matrix: List[List[str]]) -> None:
    for i in range(len(matrix)):
            print(' '.join(matrix[i]))
'''
abca
efgh
ijkl
mnop
t=d
'''
def rotate_matrix(matrix: List[List[str]]) -> None:
    n = len(matrix)
    for layer in range(n//2):
        for i in range(layer,n-1-layer):
            temp = matrix[layer][n-1-i] # temp = top
            matrix[layer][n-1-i] = matrix[i][layer] # top = left
            matrix[i][layer] = matrix[n-1-layer][i] # left = bottom
            matrix[n-1-layer][i] = matrix[n-1-i][n-1-layer] # bottom = right
            matrix[n-1-i][n-1-layer] = temp # right = temp

dim = 5
matrix = [[chr(97+dim*i+j) for j in range(dim)] for i in range(dim)]
print_matrix(matrix)
rotate_matrix(matrix)
print()
print_matrix(matrix)

#implement copy solution, and just use assert to compare? nah

# again
'''
rotate matrix 90 degrees counter clockwise
a b c d e
e f g h
i j k l
m n o p

d h l p
c g k o
b f j n
a e i m

time: O(n**2)
space: go for O(1)
time: 8:00am -- 8:18am = 18mins
d is the head

for layer in range(n // 2)
    for i in range(n-1-layer-2)
        temp = a[layer][i]
        a[0][i] = a[i][n-1]
        a[i][n-1] = a[n-1][n-1-i]
        a[n-1][n-1-i] = a[n-1-i][0]
        a[n-1-i][0] = temp
'''
from typing import List


def rotate(a: List[List[str]]) -> None:
    n = len(a)
    for layer in range(n // 2):
        for i in range(layer, n-1-layer):
            temp = a[layer][i]
            a[layer][i] = a[i][n-1-layer]
            a[i][n-1-layer] = a[n-1-layer][n-1-i]
            a[n-1-layer][n-1-i] = a[n-1-i][layer]
            a[n-1-i][layer] = temp

dim = 4
a = [[chr(4*j + i +97) for i in range(4)] for j in range(4)]
for i in range(dim):
    print(' '.join(a[i]))
rotate(a)
for i in range(dim):
    print(' '.join(a[i]))



'''
lesson learned: 
you have to define well what the solution looks like even before pouncing into 'pseudocode' which really isn't but just trying to recollect memorized!


Given an image represented by an NxN matrix, rotate it

a b c d e
0 1 2 3 4
f g h i j
5 6 7 8 9
k l m n p

top: 
'''
from typing import List


def rotate_image(matrix: List[List[str]]) -> None:
    n = len(matrix)
    for peel in range(n // 2):
        for k in range(1 + peel, n-peel):
            temp = matrix[peel][k]
            matrix[peel][k] = matrix[n-1-k][peel]
            matrix[n-1-k][peel] = matrix[n-1-peel][n-1-k]
            matrix[n-1-peel][n-1-k] = matrix[k][n-1-peel]
            matrix[k][n-1-peel] = temp

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
]
rotate_image(matrix)
print(matrix)

'''
going to rotate a matrix counter clockwise, via multiple transformations

1 2 3 4 5
a b c d e  c = 1,2
6 7 8 9 0. 7 = 2,1
g h i j k
^ & * ( )

4 should end up at where a is: 1,0

flip over the 45 degree diagonal (transpose): a_ij <-> a_ji, i < j
then flip horizontally: aij <-> a_(n-1-i)_j, i in [0,n//2)
'''
from typing import List


def rotate_matrix(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n):
            if i < n // 2:
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

'''
0 1 2  
3 4 5
6 7 8

6 1 2  
3 4 5
0 7 8

final ans should be
2 5 8
1 4 7
0 3 6
'''
n = 3
# matrix = [[i*n+j for j in range(n)] for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()
# print()
# rotate_matrix(matrix)
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()


from random import randrange
n = 5
matrix = [[randrange(10) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print()
rotate_matrix(matrix)
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
