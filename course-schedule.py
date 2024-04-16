'''
courses 0..n-1

10 01

15  23 34 42
85

if there is a cycle, return false. 
otherwise return true
1. build the graph
2. from each node, visit the graph. but if you hit someone
already visited who isn't your parent, then it is over
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        nbs {3[12] 1[4] 2[4]}
        vis {}
        call 
        iscycle  2 {2} | 4 {24}
            1<--3<--5
            v   ^   ^
            4<--2---

        '''
        def iscycle(node: int, vis: Set[int]) -> bool:
            vis.add(node)
            ans=False
            for nb in nbs[node]:
                if nb in vis or iscycle(nb,vis):
                    ans=True
                    break
            vis.remove(node)
            return ans

        nbs=defaultdict(list)
        for node,nb in prerequisites:
            nbs[node].append(nb)
            nbs[nb]
        for node in nbs:
            if iscycle(node,set()):
                return False
        return True
