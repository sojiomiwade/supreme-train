'''
idx 0 1 2 3  4 5 6 7
arr 2 3 0 1  5 3 6 7
          ^
idx  7
arr  7

initializer
    two queues
in loop i
    check if new idx to topidx is too much. if so pop the top
    drill through as long as new el is more than back
    append top of queue only when i >= k-1

idx 0 1 2 
arr 7 2 4
        idx
idxq  [2]
numsq [4]
ans [7]
expected = [7,4] k = 2

'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idxq,numsq=deque([]),deque([])
        ans=[]
        for idx,num in enumerate(nums):
            if idxq and idx-idxq[0]+1 > k: # 7 2 
                idxq.popleft()
                numsq.popleft()
            while numsq and numsq[-1]<num:
                idxq.pop()
                numsq.pop()
            idxq.append(idx)
            numsq.append(num)
            if idx>=k-1:
                ans.append(numsq[0])
            # print(idx, num, numsq)
        return ans