'''
take element x in arr1 (do below for each)
now find the element closest to it. if the dist between both is <=d, 
then that x doesn't count

 4
1 8 9 10

 5         55
 2
1 8 8 8 8 8 99
  i

bl -> check i and i-1
br -> check i and i-1

  x-----y--z---k
   ------------
 find all 
45
do a binary search for each arr1: mlgm, where m is the number of elements in arr1
'''
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n,count=len(arr2),0
        arr2.sort()
        for x in arr1:
            i=bisect.bisect_left(arr2,x)
            if ((not 0<=i<n or abs(arr2[i]-x)>d) and
                (not 0<=i-1<n or abs(arr2[i-1]-x)>d)):
                count+=1
        return count

        