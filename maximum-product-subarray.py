'''
2 3 -2   5  2  3   4   4   0 1 5
2 6 -12           -99 -99  0 1 5
array a: go forward aggregating, if you see 0, set that to 0                            
array b: go backward, same thing
return the max in a+b

-6  6  3  0  1 
-1  2  3  0  1
-1 -2 -6  0  1       
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        forward=[0 for _ in range(n)]
        backward=[0 for _ in range(n)]
        forward[0],backward[-1]=nums[0],nums[-1]
        for i in range(1,n):
            if forward[i-1]:
                forward[i]=forward[i-1]*nums[i]
            else:
                forward[i]=nums[i]
            j=n-i-1
            if backward[j+1]:
                backward[j]=backward[j+1]*nums[j]
            else:
                backward[j]=nums[j]
        return max(itertools.chain(forward,backward))
