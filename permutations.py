class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case and build
        # abcdefg
        #  num
        # last=[[a]]
        # lis=[ a ]
        #      ^ ^
        # lislen=2 
        # cur=[[ba],[ab]]
        # cba 
        # T(n): n * (n-1)! * n * n = n**2 * n! <--upper bound
        #   as last is not fixed n!
        # 1 2 32 432
        last=[[]]
        cur=[]
        n=len(nums)
        for num in nums:
            for lis in last:
                for i in range(1+len(lis)):
                    cur.append(lis[:i] + [num] + lis[i:])
            last,cur=cur,[]
        return last


        # try prefix approach
        '''
        12345
        pre : 1-5
        rem : 2345
               ^ 
        add2prefix(1,2345)
        add2prefix(2,1345)
        add2prefix(3,1245)
        ...
        add2prefix(32,145)
        for i in range(len(rem)):
            permute(prefix+rem[i], rem[:i]+rem[i+1:])
        123
        123
        132
        213
        T(n) = n*T(n-1) + n**2
           n * ((n-1)*T(n-2)+(n-1)**2) + n**2
           n * n-1 * T(n-2) +    n*n-1 + n**2
           n! + n**3
        '''
        # def permute(prefix: List[int], rem: List[int]) -> None:
        #     if not rem:
        #         ans.append(prefix)
        #         return
        #     for i in range(len(rem)):
        #         permute(prefix+[rem[i]], rem[:i]+rem[i+1:])
        # ans=[]
        # permute([],nums)
        # return ans

        # def permute(idx: int, bidx: int) -> None:
        # DFS graph approach
        #     buf[bidx]=nums[idx]
        #     visited[idx]=True

        #     if bidx==n-1:
        #         ans.append(buf[:])

        #     for i in range(n):
        #         if not visited[i]:
        #             permute(i,bidx+1)

        #     visited[idx]=False

        # n=len(nums)
        # visited,buf=[False for _ in range(n)],[0 for i in range(n)]
        # ans=[]
        # for i in range(n):
        #     permute(i,0)
        # return ans