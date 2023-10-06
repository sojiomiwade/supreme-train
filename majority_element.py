'''
[2,2,1,1,1,2,2]
1 1 1 2 2 2 2  n = 7 => floor(n/2) = 3
0 1 2 3 4 5 6 
      ^


1 1 1 1 2 2 2  n = 7 => floor(n/2) = 3
0 1 2 3 4 5 6 
      ^

1 1 2 2 2 2  n = 7 => floor(n/2) = 3
0 1 2 3 4 5 
    ^

1 1 1 1 2 2  n = 7 => floor(n/2) = 3
0 1 2 3 4 5 
    ^
sort it. then it is arr[floor(n/2)]      

3 2 3
count: 
maxf 
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def me_bysort():
            return sorted(nums)[len(nums) // 2]
        def me_by_count():
            count = Counter()
            maxf = 0
            res = None
            for el in nums:
                count[el] += 1 # {2:1 , 3:2}
                if count[el] > maxf: 
                    maxf, res = count[el], el # 2,3
            return res

        return me_by_count()
