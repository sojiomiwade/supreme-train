'''
idx 0 1
arr 1 1
    ^
vis {0 1}
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def canreach(idx):
            if not 0<=idx<n or idx in vis:
                return False
            vis.add(idx)
            if arr[idx]==0:
                return True
            return canreach(idx-arr[idx]) or canreach(idx+arr[idx])

        n,vis=len(arr),set()
        return canreach(start)