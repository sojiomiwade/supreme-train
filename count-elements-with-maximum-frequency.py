'''
1 2 2 3 1 4
count {12 22 31 41}
maxf 2
count 2
if freq is equal to maxf increment count, 
else if it is more reset count to 1, and increment maxf
return maxf * count

1 2 2 3 1
        ^
count {12 22 31}
maxf 2
maxcount 2
count 
'''
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter()
        maxf=0
        maxcount=0
        for num in nums:
            count[num]+=1
            if count[num]==maxf:
                maxcount+=1
            elif count[num]>maxf:
                maxcount=1
                maxf+=1
        return maxf*maxcount
            