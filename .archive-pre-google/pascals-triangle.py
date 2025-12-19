'''
numRows=5
1
1 1
1 2 1 | m = 3
1 3 3 1
1 4 6 4 1 <--5

m=5 is number of rows in that row
rows.append([1])

for m in (2..5+1)
    rows.append(array of size m, all values=1)
    j in [1..m-1)
        row[-1][j]=row[-2][j]+row[m-1][j-1]
numRows=5
[1]
[1 1]
[1 2 1]
[1 1 1 1]
[1 1 1 1 1]
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows=[]
        for m in range(1,numRows+1):
            rows.append([1 for _ in range(m)])
            # print(rows,m)
            for j in range(1,m-1): # 1,2,3
                rows[-1][j]=rows[-2][j]+rows[-2][j-1]
        return rows
