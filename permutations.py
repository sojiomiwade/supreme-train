class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(idx: int, bidx: int) -> None:
            buf[bidx]=nums[idx]
            visited[idx]=True

            if bidx==n-1:
                ans.append(buf[:])

            for i in range(n):
                if not visited[i]:
                    permute(i,bidx+1)
                    
            visited[idx]=False

        n=len(nums)
        visited,buf=[False for _ in range(n)],[0 for i in range(n)]
        ans=[]
        for i in range(n):
            permute(i,0)
        return ans