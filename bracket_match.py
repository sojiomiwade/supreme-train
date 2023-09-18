'''
time: 
time comp:
space comp:
key ob: don't let res get negative; start it at 0 
alg: 
))((()()))
    ^


A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
left 1/0/1
right 1
right will never go down if unmatched. 
left is just number of residual left
return left + right

loop:
    if (
        resid_left ++   # 1/0/1
    else )
        if resid_left > 0
            resid_left --
        else
            right ++        # 1
output: 2
Constraints:

[time limit] 5000ms

[input] string text

1 ≤ text.length ≤ 5000
[output] integer

'''


def bracketMatch(s: str) -> int:
    resid_left = right = 0
    for ch in s:
        if ch == '(':
            resid_left += 1
        else:
            if resid_left > 0:
                resid_left -= 1
            else:
                right += 1
    return resid_left + right

text = '(()'
print(bracketMatch(text)) # 1
text = '(())'
print(bracketMatch(text)) # 0
text = '())('
print(bracketMatch(text)) # 2

