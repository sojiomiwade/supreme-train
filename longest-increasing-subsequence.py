'''
10 9  2  5  3  7  25 18
10 25
9 25
2 5 7 25
2 3 7 25
2 3 7 25

2, 6, 8, 3, 4, 5, 1 0 2 6 6
-        -  -  -        -
2 3 4 5 6
1 2
0

another maybe simpler way is have two arrays
one owrite, write: owrite is the one to tell the length
write takes on new elements, 
if owrite will add a new elem, write it in both.
otherwise only update owrite
no ... this won't work: should have thought it through before writing it down


the true sequence is under the overrides
use a parent map p[0]=1, p[1]=(2,0), p[2,0]=None
the elements can just be tuples (the number and its ans idx)
for each i, element
    while parent(element)
        element=parent[element]
    ans[i]=element

now in original problem
    (val,len(ans)-1)
    on append -- parent[element]=None
    on overwrite -- parent[element]=prevelement

return [key for key in ans]

bisect left, so existing number is overwritten
if ans == n, then append
2 3
max=3

another maybe simpler way is have two arrays
one owrite, write: owrite is the one to tell the length
write takes on new elements, 
if owrite will add a new elem, write it in both.
otherwise only update owrite
3 6 8 .. 2
2 .. 2
nums 7 7 
ans 

'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        write=[]
        for num in nums:
            if not ans or ans[-1]<num:
                ans.append(num)
                write.append(num)
            else:
                idx=bisect.bisect_left(ans,num)
                ans[idx]=num
        return len(ans)

