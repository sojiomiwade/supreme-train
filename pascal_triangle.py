'''
1
1 1
1 2 1 -- i+1 = 3
1 3 3 1
1 4 6 4 1
1 -- 1
2 -- 2/2 -- 1
3 -- 3/2
r(i,j) = r(i-1,j) + r(i-1,j-1)
use zero if either is undefined
time: each row is O(r(i))
total number of elements is n^2
hence: O(n**2), likewise space for the result
run it: 
[1],[1,1],[1,2,1],[1,3 ,   3  ,1]
[1], [1,1], [1, 2,1]
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows): # 0,1,--2
            res.append([1 for i in range(i+1)]) #[1],[1, 1],[1,1,1]
            for j in range(1,i): # 1
                res[-1][j] = res[-2][j]+res[-2][j-1]
        return res


#--------try again------
'''
1       
1 1
1 1 1       #i=2,n=3
  j
1 3 3 1 #i = 3
  1 2

res = []
for i in range(num_rows): #i=2
    res.append([1 for _ in range(i+1)]) #[1 1 1]
    for j in range(1, i)  #j=1,
        res[-1][j] = res[-2][j] + res[-2][j-1]
return res

   1
  1 1
 1 2 1
1 3 3 1

'''

num_rows = 5
res = []
for i in range(num_rows): #i=2
    res.append([1 for _ in range(i+1)]) #[1 1 1]
    for j in range(1, i):  #j=1
        res[-1][j] = res[-2][j] + res[-2][j-1]
print(res)

