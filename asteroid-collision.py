class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for x in asteroids:
            if x>0:
                st.append(x)
            else:
                while st and st[-1]>0 and -x>st[-1]:
                    st.pop()
                if not st:
                    st.append(x)
                else:
                    top=st[-1]
                    if top==-x:
                        st.pop()
                    else:
                        if top<0:
                            st.append(x)
                        else:
                            assert top>-x
        return st
