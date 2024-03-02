'''
-4 0 3
16 0 9
0 9 16 <-- expected
nums2 16 0 9
min max 0 16
ansidx 0 ..9.. 16 
ansval 0 ..9.. 16 

2 -2 -3
f[0]=2
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minval,maxval=min(nums,key=lambda x:x**2),max(nums,key=lambda x:x**2)
        minval,maxval=abs(minval),abs(maxval)
        freq=[0 for x in range(minval,maxval+1)]
        for x in nums:
            freq[abs(x)-minval]+=1
        finalans=[]
        for x in range(minval,1+maxval):
            for fcount in range(freq[x-minval]):
                finalans.append(x**2)
        return finalans
        # return sorted (x**2 for x in nums)