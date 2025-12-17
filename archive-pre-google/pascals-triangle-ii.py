'''
ri 3
0   [1]
1   [1 1]
2   [1 2 1]
ans [1 3 3 1]
1 3 3 1
1 4 6 4 1
temp 3
oldak 1

    oldak=a[k]
    a[k]=temp+a[k]
    temp=oldak


1 4 6 4 1

temp 3
3 [1 3 3 1]
4
initialize one array to have ri+1 elements with 1's everywhere


now do all r in 1 .. ri-1 times
    and do k from 1 .. r:
        temp2 = ans[k-1]
        temp1 = ans[k] + ans[k-1]

return ans

ri 3 | exp [1 3 3 1]
ans [1 3 3 1]
k 2 [1 2]       
oldak,temp 1,1
r 2 [1 2]
'''
class Solution:
    def getRow(self, ri: int) -> List[int]:
        ans=[1]*(1+ri)
        for r in range(1,ri):
            temp=1
            for k in range(1,1+r):
                oldak=ans[k]
                ans[k]+=temp
                temp=oldak
        return ans