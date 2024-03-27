'''
    -----------------
0   1   2   3   4   5
1   0   0   1   0   1
1  -1  -1   1  -1   1
1   0  -1   0  -1   0

111|3|
stream 1 1 0 0 1 1
prefix 1 2 1 0 1 2

3 - (-1+1) + 1

l {0:-1}
idx,val:
    idx - l[val]

0  1  0
-1 0 -1
      p
ans 2
il {0:-1 -1:0 }
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        il=dict({0:-1})
        prefix=ans=0
        for idx,val in enumerate(nums):
            prefix+=1 if val==1 else -1 
            il.setdefault(prefix,idx)
            ans=max(ans,idx-il[prefix])
        return ans
        '''
        make transformation, and use prefix sum to get lengths
        '''