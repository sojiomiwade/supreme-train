'''
st 2 2 2 1 5
aux 2 2 2 1

pop(x): if top of aux is x, then pop from aux as well
push(x): 
    push x onto st
    if x is smaller than aux, no action on aux. 
    otherwise, push x on aux
'''
class MinStack:

    def __init__(self):
        self.st,self.aux=[],[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.aux and val>self.aux[-1]:
            return
        self.aux.append(val)

    def pop(self) -> None:
        val=self.st.pop()
        if self.aux[-1]==val:
            self.aux.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.aux[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()