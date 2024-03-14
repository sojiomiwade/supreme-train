'''
        count=Counter({0:1})
        ans=0
        prefix=0
        for x in nums:
            prefix+=x
            ans+=count[prefix-goal]
            count[prefix]+=1
        return ans
1 1 0 0 0 
1 1 0 0 0 1 1
        x
p 3
ans 2 <--- c[p-2]
c {(01) (11) 22 31}

1 + 2
1 1 0 0 1
        x
1 0 1 0 1 goal 2
        x

1 1 0 0 1

p 3
ans 2 + c[1] <-- c[p-g]
c {01 12 22}


p

  s

0 0 0 0 0

000000 | goal 0
  i

ans 3
c {03}


i
res 
c {0:1, 1:2}

10101
 1
-----
psum 3
res 2 + c[3-2]
   i
c {0:1,1:2,2:2,3:1}
psum 2
res 2
2 0 0 2 1 2<--- 6
    x
p 4
ans 2
count {01 22 41 61}
ans+=count[prefix-goal]
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=Counter({0:1})
        ans=0
        prefix=0
        for x in nums:
            prefix+=x
            ans+=count[prefix-goal]
            count[prefix]+=1
        return ans