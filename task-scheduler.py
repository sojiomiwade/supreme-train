'''
4a 4d 3b 2c, n = 5
objective: calculate idles
then ans is number of tasks + idles

layout a map with a at ends
a d . . . .  a d . . . . a d . . . . a d, n = 5
all open idles: (n-xwidth+1)*(xcount-1) 5-2
used-up-idles --> m-(xcount*xwidth)
idles equals: maximum of zero and difference between open and used

a b c d a b, [n 1] -->
a b a c b d --> 6

a b . a b
m 6
xcount 2
xwidth 2
openidles (1-2) neg
used
idles

a a a b b b

a b . . a b . . a b , [n 3]
count {a3 b3}
xcount 3
xwidth 2
openidles (3-2)*(2)
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m=len(tasks)
        count=Counter(tasks)
        xcount=max(count.values())
        xwidth=sum(1 for x in count.values() if x==xcount)
        openidles=(n-xwidth+1)*(xcount-1)
        used=m-(xcount*xwidth)
        idles=max(0,openidles-used)
        return m+idles