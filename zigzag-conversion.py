'''
p   a
a p l
y  

add to ans[row]
increment row by dir
when row is at 0 change dir to +1
when row is at numrows, dir to -1

expect
p   a
a p l
y
=pa|apl|y
row,dir=1,1
s=abc, numrows=1
  i
ans=[[A]]
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        ans=[[] for _ in range(numRows)]
        dir=1
        row=0
        for ch in s:
            ans[row].append(ch)
            if numRows==1:
                dir=0
            elif row==numRows-1:
                dir=-1
            elif row==0:
                dir=1
            row+=dir
        finalans=[]
        for ansrow in ans:
            for elem in ansrow:
                finalans.append(elem)
        return ''.join(finalans)