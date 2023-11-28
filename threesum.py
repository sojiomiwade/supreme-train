'''
-1,0,1,2,-1,-4
-1,0,1,2,-1,-4
take one number and find 2sum equal to the -ve of that number
-1 
space: O(n)
time: O(n**2)

also n**2, is sort the array. 
this is also n**2 space comp
now if we have
a       b   ...    c 
        l          r
for a in range(n):
    b=a+1
    c=n-1
    three=nums[a]+nums[b]+nums[c]
    while b < c:
        if three == 0:
            res.append([nums[a],nums[b],nums[c]])
            b+=1
            c-=1
        elif three < 0:
            b+=1
        else:
            c-=1
return res

-1,0,1,2,-1,-4
-4 -1 -1 0 1 2
       a           
         b 
           c
[[-1,-1,2],[-1,0,1]]

-1   -1 0  2 2
        b

0 -> 1 -> 
1
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for a in range(n):
            if a>0 and nums[a]==nums[a-1]:
                continue
            if nums[a]>0:
                break
            b,c=a+1,n-1
            while b < c:
                three=nums[a]+nums[b]+nums[c]
                if three == 0:
                    res.append([nums[a],nums[b],nums[c]])
                    csol,bsol=c,b
                    while b<n and nums[b]==nums[bsol]:
                        b+=1
                    while c>=0 and nums[c]==nums[csol]:
                        c-=1
                elif three < 0:
                    b+=1
                else:
                    c-=1
        return res        