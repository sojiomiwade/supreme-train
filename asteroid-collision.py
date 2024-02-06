'''
2 5 -> 2 5
-5 ... 5 -> -5 5


resm:
10 2 -5
st= 10

another example: 
5 10 20 -5
st = 20 10 5

final example
4 3 2 1 -4 -2 -1
st = -1 -2
resl = from left remove all negative to the first positive (exclusively)
resr = from right remove all positive to the first negative (exclusively)
resm  is a stack when we have new element 
    if st empty or sign is the same, just add the elem
    if sign is different, keep the bigger of the two only on the top
at the end reverse the stack to form resm
res = resl + resm + resr

-2 -3 ... 5 4 -5 
come back to address 0. 
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)

        st=[]
        '''
        1 -2 1 -1
        -ve +ve => no fight
        -ve -ve +ve (-ve)
        actually, only -ve's fight!
        5 -3 -> 5
        -3 5 -> -3 5
        -2 1
        -5 2
        l 
                r
        x +ve +ve -ve
        9 8 3 2 -5
        '''
        for cur in asteroids:
            if cur>0:
                st.append(cur)
            else:
                while st and st[-1]>0 and -cur>st[-1]:
                    st.pop()
                if not st or st[-1]<0:
                    st.append(cur)
                elif st[-1]==-cur:
                    st.pop()

        return st