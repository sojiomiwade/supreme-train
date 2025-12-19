'''
implement a stack with an array
'''
from typing import List, Optional, Tuple
 

class Stack:
    class Element:
        def __init__(self, val: int, data: str) -> None:
            self.key = val
            self.data = data

    def __init__(self, size) -> None:
        self.size = size
        self.curr_index = -1
        self.arr = [self.Element(0,'') for _ in range(size)]

    def peek(self) -> Tuple[int, str]:
        if self.curr_index == -1:
            raise IndexError('pop from empty stack')
        res = self.arr[self.curr_index]
        assert type(res) is self.Element
        return res.key, res.data

    def is_empty(self) -> bool:
        return self.curr_index == -1

    '''
            01234 56789
self.arr    abcde f
size = 10         ^
    '''
    def push(self, key: int, data: str) -> None:
        if self.curr_index == self.size - 1:
            newspace = [self.Element(0,'') for _ in range(self.size)]
            self.arr += newspace
            self.size = 2 * self.size
        self.curr_index += 1
        self.arr[self.curr_index].key = key
        self.arr[self.curr_index].data = data

    def pop(self) -> Tuple[int, str]:
        item = self.peek()
        self.curr_index -= 1
        return item

stack = Stack(100)
try:
    print(stack.peek()) # raise exception
except IndexError as ie:
    print('expected', ie)
else:
    raise Exception('IndexError expected')
    
stack.push(42, '42')
stack.push(1, 'a')
stack.push(2, 'b')
print(stack.peek()) # 2b
print(stack.pop()) # 2b
print(stack.pop()) # 1a
print(stack.peek()) # 42
print(stack.pop()) # 42
try:
    print(stack.peek()) # raise exception
except IndexError as ie:
    print('expected', ie)
else:
    raise Exception('IndexError expected')

try:
    print(stack.pop()) # raise exception
except IndexError as ie:
    print('expected', ie)
else:
    raise Exception('IndexError expected')

