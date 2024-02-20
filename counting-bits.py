'''
0
2
3 011
4 100 1 more bit than arr[2]
5 101 1 more bit than ceil(5/2) ==> res[if n odd take floor then add 1]
6 110 1 more bit than arr[3]
8 special case? n&(n-1)==0? => bit count is 1
    or if arr[4] has 1 bit, then i also have 1


6 110
7 111 --> 7/2 = 3
8 1000
9 1001
0 1010 

2 4 8 16 same number
5 10 20 40 <-- same number
7 same number as 7//3 but add 1 since you lost 1
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0 for _ in range(1+n)]
        for x in range(1+n):
            ans[x]=ans[x//2]+x%2
        return ans