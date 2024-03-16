'''
 0011
54345
 1100
56765 

idx  -1 0 1
nums    1 0
count 0 1 0


idx     1  2  3  4  5  6  7  8  9
nums    0  1  1  1  1  1  0  0  1
count  -1  1  2  3  4  5  4  3  4   
       
count -1 
table {00 -11 11 23 34 45 56}
maxlen 0
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen=count=0
        seen={0:-1}
        for i in range(len(nums)):
            count+=1 if nums[i] else -1
            if count in seen:
                maxlen=max(maxlen,i-seen[count])
            else:
                seen[count]=i
        return maxlen