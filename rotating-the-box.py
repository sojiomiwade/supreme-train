'''
transform the matrix
    1 2 3 4
    5 6 7 8
    a b c d

    a 5 1  
    b 6 2  
    c 7 3  
    d 8 4  

    ij -> m-i-1, j
    loop old cols into new rows
    for j in cols
        for i in rows
            new[j][i]=new[i][j]

apply gravity (sort): 
    # . * # . . * 
    . # * . . # *
    loop on idx i, and inner loop will set i after a star
    inner loop: just a sort: l starts at i, r moves, and swap when . found
'''
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n=len(box),len(box[0])
        for rowidx in range(m):
            left=0
            for right in range(n):
                if box[rowidx][right]=='*':
                    left=right+1
                elif box[rowidx][right]=='.':
                    box[rowidx][right],box[rowidx][left]=box[rowidx][left],box[rowidx][right]
                    left+=1
        ans=[['']*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][m-i-1]=box[i][j]
        return ans
