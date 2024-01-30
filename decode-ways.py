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
            023     3
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
  1 0 6
  1 1   

23421

 1 2
 1 (1+1)

1 0
1 (0+1)

7 3
1 (1+0)

  0 3 5 
0 0 

1 0 3
1 1 1 
JC 

0 3 5 6
0 0 

1 2 3 4
123 4
123 4
1 2 3  4

226 3

...
AAB
112 = 
J
12

02
0
...

          035
        /     \
       0*       0* 
dpi = dpi2 + 1<=5<=9 dpi1

    1 3 5
1 | 1 2 2
13 5
1 3 5

0 1 3 5
0 0 0 .

1 0 3
1 

dp[i] = last_two_flag * dp[i-1]

10 1
1 0 0
1

1 3 5
1 2 2+



dp[i]=double_valid*dp[i-2] + single_valid*dp[i-1]

  1        2
1 1*1+0=1  1*1+1*1=2
1 + 3
13 

  0      3        5
1 0+0    0+0      
              035
              0
           /       \


'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0 for _ in range(1+n)]
        dp[0]=1
        for i in range(1,1+n):
            single_valid=1<=int(s[i-1])<=9
            dp[i]+=single_valid and dp[i-1]
            double_valid=i-2>=0 and 10<=int(s[i-2:i])<=26
            dp[i]+=double_valid and dp[i-2]
        return dp[n]


        # def numdecodings(i: int):
        #     if i>=n:
        #         assert i==n
        #         return 1
        #     if i in dp:
        #         return dp[i]
        #     two=0
        #     if i+1<n and 10<=int(s[i:i+2])<=26:
        #         two=numdecodings(i+2)
        #     one=0
        #     if 1<=int(s[i])<=9:
        #         one=numdecodings(i+1)
        #     dp[i]=one+two
        #     return dp[i]
        # dp,n={},len(s)
        # return numdecodings(0)