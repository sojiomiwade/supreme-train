'''
aajf
1 1106

            12
            / \
           1  12
           |   |
           2   .
           |
           .
result here is valid_2-extract plus result of a valid_1-extract
              123
             /    \
            23     3
            |\     |  
            3 .    .
            |
            .

            106
            / \
           06    6
          /0 \0     
2
23
i i+1
        1 0 6
        / . .\
       06     6
                \ 1     

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        def numdecodings(i: int):
            if i>=n:
                assert i==n
                return 1
            if i in dp:
                return dp[i]
            two=0
            if i+1<n and 10<=int(s[i:i+2])<=26:
                two=numdecodings(i+2)
            one=0
            if 1<=int(s[i])<=9:
                one=numdecodings(i+1)
            dp[i]=one+two
            return dp[i]
        dp,n={},len(s)
        return numdecodings(0)