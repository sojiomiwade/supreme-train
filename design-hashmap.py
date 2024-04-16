from typing import Optional, Tuple

class Node:
    def __init__(
        self, 
        key: Optional[int],
        val: Optional[int], 
        nextnode: Optional['Node'],
        ) -> None:
        seelf.key = key
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
