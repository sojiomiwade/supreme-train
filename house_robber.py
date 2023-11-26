'''
loot=max(nums[i]+loot(i+2),loot(i+1))
  0 1 2 3 4
0 1 
1
2
3
    1
  /
x
  \
     0

13 -- 35 36 37
57 58

p=13 + 35 + 57 + 79
p=13 + 36 + 68

14   

15

24   

25

0 1 2 3
3 4 5 6

3 + 5 = 8
  + 6 = 9
4 + 6 = 10
5     = 5

0 1 2
3 4 5
n=3
l[-1 -1 -1]
m=0
rob(0)
    m=0
    5=rob(2)
'''
class Solution:
  def rob(self, nums: List[int]) -> int:
    def rob(h):
      if l[h] is not None:
        return l[h]
      m=0
      for oh in range(h+2,n):
        m=max(m,rob(oh))
      l[h]=m+nums[h]
      return l[h]

    n=len(nums)
    l=[None for h in range(n)]
    m=0
    for h in range(n):
        m=max(rob(h),m)
    return m
'''

                    0
           2      3     4   5   6
          4 5 6  5  6

                    1
           3      4      5      6
         5   6
--
                    0
                1           2
             2    3        3    4
--
T(n)=T(n-1) + T(n-2) + C
     = 2T(n-2) + T(n-3) + 2c
      =2c + 2T(n-3) + 2T(n-4) + T(n-3) + 2c
      =3T(n-3) + 2T(n-4) + 4c
      =...

0 1 2 3 
4 5 6 7

p3=7
p2=max(n2+p4,p3)
r(0)
  |
  4 + r(2)
      |     \
      6+r(4)     r(3)
          |    |      \
          0    7+r(5)  r(6)
                  |      |
                  0      0
r(1)
  |       \
  5+r(3)  r(2)
    |     7
    7
   
0 1 2 3
        h
'''
class Solution:
  def rob(self, nums: List[int]) -> int:
    def rob(h):
      if h>=n:
        return 0
      if dp[h] is not None:
        return dp[h]
      dp[h]=max(nums[h]+rob(h+2),rob(h+1))
      return dp[h]

    n=len(nums)
    dp=[None for h in range(n)]
    return rob(0)