class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        1 4 2 3
        find maxidx in (curlen, 1, -1)
            flip(arr,maxidx+1)
            flip(arr,curlen)
        '''
        def flip(k: int) -> None:
            for i in range(k//2):
                j=k-1-i
                arr[i], arr[j] = arr[j], arr[i]

        def findmaxidx() -> int:
            maxidx, maxval=-1, float('-inf')
            for i in range(curlen):
                val = arr[i]
                if val > maxval:
                    maxidx, maxval = i, val
            return maxidx
                
        '''
        1 4 2 3
        4123
        3214
        3214
        1234
        ans=[2,4,1,3,2,2]
        '''
        n = len(arr)
        ans = []
        for curlen in range(n, 1, -1):
            maxidx = findmaxidx()
            flip(maxidx + 1)
            flip(curlen)
            ans.extend([maxidx + 1, curlen])
        return ans