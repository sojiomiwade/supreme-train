'''
11106
            .
         /     \
1 1106
    1  106
        10 6
             .+1  0
nw(s) is nw(s[1:]) if you can remove a valid char plus (only 0 not ok)
         nw(s[2:]) if you can remove 2 valid chars 23 ok but 27 not
                    10 ok but 03 not
12
ab and l
1 -- 2 -- [1]

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        def nw(s: str, idx: int) -> int:
            if idx>=n:
                assert idx==n
                return 1
            if idx in dp:
                return dp[idx]
            count=0
            if 1<=int(s[idx])<=9:
                count=nw(s,idx+1)
            if idx+1<n and 10<=int(s[idx:idx+2])<=26:
                count+=nw(s,idx+2)
            dp[idx]=count
            return count

        dp={}
        n=len(s)
        return nw(s,0)