'''
{} {[()]} -> true
    ^
))(( -> false
^
count=2

3 variables one for each bracket can use hashmap, type_count that maps either the left or the right of a type
that counter can't go negative which helps catch out of order but same number of brackets pattern
time and space: O(n), O(1)
{[()]}

brace 1
brack
paren

{}([)]
  ^
st=([)]


'''
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        left = {'}':'{', ')':'(', ']':'['}
        for ch in s:
            if st and ch in left and left[ch] == st[-1]:
                st.pop()
            else:
                #below if is only to break early, not necessary
                if ch in left:
                    return False
                st.append(ch)
        return not st