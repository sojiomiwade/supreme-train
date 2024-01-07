'''
      3 4 5
h o r s e
r o s
    2
insert into w2: advance i
delete from w1: advance i
insert into w1: advance j
delete from w2: advance j
replace: advance on both i and j

md(i,j) = 
    md(i+1,j+1) if word1[i]==word2[j]
    1+min(md(i+1))
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def min_distance(i: int, j: int) -> int:
            if i==m or j==n:
                return max(n-j,m-i)
            if (i,j) in dp:
                return dp[i,j]
            if word1[i]==word2[j]:
                dp[i,j]=min_distance(i+1,j+1)
                return dp[i,j]
            advancei=min_distance(i+1,j)
            advancej=min_distance(i,j+1)
            replace=min_distance(i+1,j+1)
            dp[i,j]=1+min(advancei,advancej,replace)
            return dp[i,j]

        dp={}
        m,n=len(word1),len(word2)
        return min_distance(0,0)
