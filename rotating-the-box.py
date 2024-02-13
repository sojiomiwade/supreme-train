'''
  0 1 2 3
0 # . * .
1 # # * .
2 . . . .
02 -> 21
02 -> 2(2)
23 -> 3(3-1-2) = 0
rc -> c(m-1-r)
# #
# .
* *
. .


# . # * # . #
l
  r
l moves to stationary object + 1 if r becomes one
otherwise, swap l and r items if r is space and l is stone
. # # * . # # 
###.
.###

"#",".","*","."],["#","#","*","."

# . * .     . # * .
# # * .     # # * .          us -> '#', '.', '*', '#']

# # * .
    r
l
. # # #
  l  
    r
'''
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n=len(box),len(box[0])
        rbox=[[0 for j in range(m)] for i in range(n)]
        for row in range(m):
            left=0
            for right in range(n):
                if box[row][right]=='*':
                    left=right+1
                elif box[row][right]=='.':
                    box[row][left],box[row][right]=box[row][right],box[row][left]
                    left+=1
        for r in range(m):
            for c in range(n):
                rbox[c][m-1-r]=box[r][c]
        return rbox