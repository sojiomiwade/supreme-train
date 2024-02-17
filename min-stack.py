-2 0 -3
(-2 -2) (0 -2) (0 -3)

g p t g : -3 n 0 -2
on push: if stack empty, can just push (el,el)
    otherwise, push (el,min(el,stack[-1]))
on pop: remove top of stack 
top: return top of stack's first arg
getMin : return top of stack's 2nd arg
time comp of all ops is O(1)

2nd way: use 2nd stack to track only the mins
-2 0 -3
-2 -3
key, 
push: push onto minstack only if no minst or cur less than minst[-1]
    otherwise dont
pop: pop from minst if st[-1] equals minst[-1]
