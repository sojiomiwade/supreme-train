'''
invalid: {(})
valid: {()}
=>same number of brackets won't suffice
first: just use a stack: push for left, pop for right, 
pop fails if the left of the cur is not on the top
if at the end, stack still has elements, fail
second: use 3 variables instead of stack
{([( )])}
}{}
0123
hmm.. still need to track locations it seems
'''
class Solution:
    def isValid(self, s: str) -> bool:
        left={']':'[','}':'{',')':'('}
        st=[]
        for x in s:
            if x in '([{':
                st.append(x)
            else:
                if not st or st[-1]!=left[x]:
                    return False
                st.pop()
        return not st