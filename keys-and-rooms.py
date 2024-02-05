'''
0 1 2 3 ... n
if len(visited)==n return true, false otherwise
DFS (or BFS) starting from 0, and just visit
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def visit(room):
            if room in visited:
                return
            visited.add(room)
            for oroom in rooms[room]:
                visit(oroom)
        # 0 -- 1
        #  \   /     
        #.   2
        # v={0,1,2s}
        visited,n=set(),len(rooms)
        visit(0)
        return len(visited)==n
