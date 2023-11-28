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
        return res        '''
-1,0,1,2,-1,-4
-4 0 1 2 -1 -1
s=2 * -1 = -2

1
{}



res={ [0 -1 1] []}

optimizations:
  * should remove duplicate numbers (with a set)
  to avoid dealing with turning each tuple into a set
  even then still need to use some kind of a sorted list
  * unless we also sort the main list (as well as remove dups)
  * now two sum should only go forward though
  * once nums[si] is not negative, can break
-4 -1 0 1 2
have={0,-1}
sum=1-1

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def find_twosum(si):
            sum=-nums[si]
            have=set()
            for i in range(si+1,n):
                if sum-nums[i] in have:
                    res.add(tuple(sorted([nums[i],sum-nums[i],-sum])))
                have.add(nums[i])

        res=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            find_twosum(i)
        return list(res)