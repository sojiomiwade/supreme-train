'''
use the indegree of each node, quadratic!
if at any point you cannot find a node with degree 0, return false
after n repeats, can just return true.

setup the graph. b is a prereq of a => b --> a
use that to get the indegree
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nbs=[[] for _ in range(numCourses)]
        indegree=Counter()
        for node,nb in prerequisites:
            nbs[node].append(nb)
        for course in range(numCourses):
            for nb in nbs[course]:
                indegree[nb]+=1
        for _ in range(numCourses):
            for i in range(numCourses):
                if indegree[i]==0:
                    indegree[i]=-1
                    for nb in nbs[i]:
                        indegree[nb]-=1
                    break
            else:
                return False
        return True