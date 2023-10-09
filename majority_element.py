'''

[2,2,1, 1 ,1,2,2]
1

221 --> 2


122 --> 2

             1
2 2 1.     11 22  3//2 = 1
  2
2   1

122
212
221

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

2,2,1  ,1,1,2,2

01

12 2

 1 x 
11 x1   22

x1
5 5/2
01 2 345
T(n) = 2 T(n/2) + n
2 (2 T(n4) + n/2) + n

2**lgn + n + ... + n = nlgn 
1234
2 1 12 -> 3/2 = 1
'''
import operator as op
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

        def bisect(lo, hi) -> int:
            '''
            323
            32, 3
            0 + (1)
            '''
            if lo == hi:
                return nums[lo]

            mi = lo + (hi - lo) // 2 #
            left = bisect(lo, mi) # 0,1
            right = bisect(mi+1, hi) # 2,2
            if left == right:
                return left
            lc = op.countOf((nums[idx] for idx in range(lo, hi + 1)), left)
            rc = op.countOf((nums[idx] for idx in range(lo, hi + 1)), right)
            return left if lc > rc else right

        def moore():
            '''
            AABA
              ^
              12
            '''
            count = 0
            res = None
            for num in nums:
                if count == 0:
                    res = num
                if num != res:
                    count -= 1
                else:
                    count += 1
            return res
        
        def bitvec():
            '''
            get distribution into array of each bit
            then go through and aggregate sum those
            ones having value greater than n/2
            agg part: if bit 4 high enough freq, then
            8 has a presence so 
            agg += (1 >> i)

            3 2 3
            '''
            def init_distro() -> List[int]:
                distro = [0] * 32
                for num in nums:
                    mask = 1
                    for i in range(32):
                        distro[i] += int(mask & num != 0)
                        mask <<= 1
                return distro

            def aggregate_majority() -> int:
                ret = 0
                mask = 1
                for i in range(32):
                    if distro[i] > len(nums)//2:
                        ret += mask
                    mask <<= 1
                '''
                11010110
                if there is a 1 in the bit-31
                then make 111...1[ret]
                which is front with 32 zeros OR ret
                (-1 << 32) | ret

                fron
                '''
                if ((1 << 31) & ret) != 0:
                    ret |= (-1 << 32)
                return ret
            distro = init_distro()
            return aggregate_majority()

        return bitvec()
