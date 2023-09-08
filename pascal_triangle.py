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
        res = [[1]]
        for i in range(1,numRows): #num=3 -- 3-1=2 -- i = 1
            a = [1] #
            for j in range(1,i): # (1,2)
                first = res[-1][j]    #[2]
                second = res[-1][j-1] # [1]
                a.append(first+second)
            a.append(1)
            res.append(a)
        return res
