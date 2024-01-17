'''
make a graph of nodes. then do a DFS. return true if you can get there
1 - 2      3

0v 1
 2
'''
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def get_validpath(node: int) -> bool:
            visited.add(node)
            if node==destination:
                return True
            found=False
            for nb in nbs[node]:
                if nb not in visited:
                    found=found or get_validpath(nb)
            return found

        nbs=defaultdict(list)
        visited=set()
        for u,v in edges:
            nbs[u].append(v)
            nbs[v].append(u)
        return get_validpath(source)