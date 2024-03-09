'''
two pointers. take topel and botel. if equal return that element
otherwise adbvance the idx with the smaller element.
when one array is done, return -1
3
t
    b
2 2
'''
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        top=bot=0
        while top<m and bot<n:
            topel,botel=nums1[top],nums2[bot]
            if topel==botel:
                return topel
            if topel<botel:
                top+=1
            else:
                bot+=1
        return -1