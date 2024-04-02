class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        L=len(tasks)
        count=Counter(tasks)
        mf=max(count.values())
        mfc=sum(1 for x in count.values() if x==mf)
        T=L-mfc
        A=(mf-1)*(n+1)
        I=A-T
        return L+max(0,I)