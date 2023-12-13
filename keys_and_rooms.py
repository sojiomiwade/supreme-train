class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        0 -> 1 -> 2 -> 3
        v = {0 1}
        '''
        def canVisitAllRooms(room):
            for oroom in rooms[room]:
                if oroom not in visited:
                    visited.add(oroom)
                    canVisitAllRooms(oroom)

        visited = set([0])
        canVisitAllRooms(0)
        return len(visited) == len(rooms)