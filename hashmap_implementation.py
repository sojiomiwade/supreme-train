'''
approach 1
use linked list for each slot, slot is an array element, so we have an array of linked lists. to minimize collisions, let's use a factor of 10 less than the worst case
'''
from typing import Optional


class MyHashMap:
    class Node:
        def __init__(
            self, 
            key: Optional[int],
            val: Optional[int], 
            nextnode: Optional[Node],
            ) -> None:
            self.key = key
            self.val = val
            self.nextnode = nextnode

        def __init__(self) -> None:
            self.headnode =

    def __init__(self) -> None:
        self.size = 1000
        self.table = [Node() for _ in self.size]

    def hashfunc(self, code) -> int:
        return code % self.size

    def put(self, key: int, value: int) -> None:
        # lis -> (new) -> temp
        nodelist = self.hashfunc(key)
        temp = nodelist.nextnode
        nodelist.next = Node(key, val, temp)
        
    def _findnode(self, key: int) -> Optional[Tuple[Node, Node]]:
        '''
        p -> x -> n
        '''
        nodelist = table[self.hashfunc(key)]
        prevnode = None
        for node in nodelist:
            if node.key == key:
                return prevnode, node
            prevnode = node
        return None

    def get(self, key: int) -> int:
        _, node = self._findnode(key)
        if node:
            return node.val
        return -1

    def remove(self, key: int) -> None:
        '''
            prev -> x -> next
            prev -> next
        '''
        prevnode, node = self._findnode(key)
        if node:
            prevnode.next = node.next

