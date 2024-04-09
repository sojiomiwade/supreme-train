'''
abBAcC
just use a stack. done!

top e
st [l ]
'''
class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for ch in s:
            top=st[-1] if st else ''
            if top.lower()==ch.lower() and top!=ch:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)
                
        