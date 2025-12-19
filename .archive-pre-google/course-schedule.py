from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def canfinish(course: int) -> bool:
            aux.add(course)
            for prereq in nbs[course]:
                if prereq not in vis:
                    if prereq in aux or not canfinish(prereq):
                        return False
            aux.remove(course)
            vis.add(course)
            return True

        nbs=[[] for _ in range(numCourses)]
        for course,prereq in prerequisites:
            nbs[course].append(prereq)
        vis,aux=set(),set()
        for i in range(numCourses):
            if not canfinish(i):
                return False
        return True
