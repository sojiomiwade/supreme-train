'''
0 1 2 3 4 5 6 7
4,3,2,7,8,2,3,1

0 --> 4 --> 8
1 --> 3 --> 7    6
<------------         
      <-----------
s
f   

1 2 3 4 5 6 7 8

6
5 --> 2 
      ><

keep nexting like a linked list, and if you hit a cycle, add that 
node, and move to next thing
0   1   2 
-1 -1   2
-1 -1   2
ans [1]
num --> nums[num-1]
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            x=abs(x)
            if nums[x-1]<0:
                ans.append(x)
            else:
                nums[x-1]*=-1
        return ans