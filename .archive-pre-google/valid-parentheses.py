'''
open brackets must be matched with same kind of bracket but the close one

( [ ( }
so if a close bracket cannot pop off the stack, return False
at the end return true only if stack (will have only opens)is emtpy
( ) { ] -> false
      ^
top {
st [{]
'''
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for bracket in s:
            if bracket in '([{':
                st.append(bracket)
            else:
                if not st:
                    return False
                top=st[-1]
                if top+bracket not in ('()','{}','[]'):
                    return False
                st.pop()
        return not st