
'''
approach 1
use linked list for each slot, slot is an array element, so we have an array of linked lists. to minimize collisions, let's use a factor of 10 less than the worst case
'''
from typing_extensions import Self
from typing import Optional, Tuple

class Node:
    def __init__(
        self, 
        key: Optional[int],
        val: Optional[int], 
        nextnode: Optional[Self],
        ) -> None:
        self.key = key
        self.val = val
        self.nextnode = nextnode

class MyHashMap:
    def __init__(self) -> None:
        self.size = 1000
        self.table = [Node(None, None, None) for _ in range(self.size)]

    def hashfunc(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, val: int) -> None:
        # lis -> (new) -> temp
        find_return_val = self._findnode(key)
        if find_return_val:
            _, node = find_return_val
            node.val = val
        else:
            head = self.table[self.hashfunc(key)]
            temp = head.nextnode
            head.nextnode = Node(key, val, temp)
        
    def _findnode(self, key: int) -> Optional[Tuple[Node, Node]]:
        '''
        p -> x -> n
        '''
        prevnode = self.table[self.hashfunc(key)]
        curr = prevnode.nextnode
        while curr:
            if curr.key == key:
                return prevnode, curr
            prevnode = curr
            curr = curr.nextnode
        return None

    def get(self, key: int) -> int:
        _findnode_return = self._findnode(key)
        if _findnode_return:
            _, node  = _findnode_return
            assert type(node.val) is int
            return node.val
        return -1

    def remove(self, key: int) -> None:
        '''
            prev -> x -> next
            prev -> next
        '''
        _findnode_return = self._findnode(key)
        if _findnode_return:
            prevnode, node = _findnode_return
            prevnode.nextnode = node.nextnode

hm = MyHashMap()
print(hm.get(2)) # -1
hm.put(2, 3)
print(hm.get(2)) # 3
hm.put(2, 5)
print(hm.get(2)) # 5
hm.remove(2)
print(hm.get(2)) # -1

hm.put(1100, 42)
hm.put(50000, 420) 
print(hm.get(2)) # 5

print(hm.get(1100)) # 42
hm.remove(1100)
print(hm.get(1100)) # -1

print(hm.get(110)) # -1
print(hm.get(50000)) # 420

print('goodbye!')
print(hm.put(100, 1))
print('goodbye again!')
print(hm.get(100))
print('goodbye seen!')
print(hm.get(1100))
print('goodbye not seen!')

