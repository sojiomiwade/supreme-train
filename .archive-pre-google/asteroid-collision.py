'''
5 10 -5 
st [5 10]

arr [-8 8]
st []

9 2 -5
9

9 2 
as long as its negative, drill into stack
    if stack top is neg, add cur
    elif it sees same el, pop stack and lose the cur 
    elif el is bigger in mag, lose the cur
    else pop the top  and keep looping as cur isn't lost
otherwise just place it on the stack, *unconditionally*

arr [8 -8]
        c
st [8]
top 8
cur -8
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i,n,st=0,len(asteroids),[]
        while i<n:
            cur=asteroids[i]
            if cur>0 or not st:
                st.append(cur)
            else: #cur<0 and there is a top 
                top=st[-1]
                if top<0:
                    st.append(cur)
                elif top==-cur:
                    st.pop()
                elif top>-cur:
                    pass
                else:
                    st.pop()
                    i-=1
            i+=1
        return st