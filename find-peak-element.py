class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        1,2,1,3,5,6,4
        1 2 3 1
            l h
            m
        if cur element isn't peak, then go binsearch in direction of any larger element
        '''
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mi=lo+(hi-lo)//2
            nums_mil=nums_mir=float('-inf')
            if mi>0:
                nums_mil=nums[mi-1]
            if mi<n-1:
                nums_mir=nums[mi+1]
            if nums[mi]>max(nums_mil,nums_mir):
                return mi
            if nums_mil>nums[mi]:
                hi=mi-1
            else:
                lo=mi+1
        raise Exception('peak element should exist')