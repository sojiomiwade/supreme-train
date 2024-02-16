'''
n=5
0 1 ... 4
bidirectional
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def validpath(v: int):
            if v==destination:
                return True
            
            visited[v]=True
            for w in nbs[v]:
                if not visited[w] and validpath(w):
                    return True
            return False

        nbs=defaultdict(list)
        for u,v in edges:
            nbs[u].append(v)
            nbs[v].append(u)

        visited=[False]*n
        return validpath(source)