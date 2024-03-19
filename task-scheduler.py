'''
"A","A","A", "B","B","B"
0 
a b i i a b i i a b

a a a b b b
0 1 2 3 4 5

a b <-- sorted keys we must iterate through of the hashmap 
3 3

a b i i 
0 1 2 3
---2
-------3

idlecount = n+1-letcount
01234

swap out idle count with something else
a a a b b b
count {a0 b0}
ans 6
idlecount 2+1-2 = 1
rem 0

a c a b d b
count {a2 b2 c1 d1}
count {a1 b1 c0 d0}
ans [a b c d 1 1 x a b ]
     0 1 2 3 4 5 6
     5+1
idlecount 3
rem 4

a a a b b b
count {a1 b1}
ans [1 1 1 | 1 1 1 | 1 1 ]
idlecount 2+1-2=2
rem 2

tasks,n : a a a b c d e f g, 1
ans [a b c d e f g a I a] = 7 + 4 = 10
a b a 
rem 0
count {a b c d e f g}
idlecount 1
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        rem=len(count)
        ans=0

        while True:
            idlecount=max(0,n+1-rem)
            for ch in count:
                count[ch]-=1
                if count[ch]>=0:
                    ans+=1
                    if count[ch]==0:
                        rem-=1
            if not rem:
                return ans
            ans+=idlecount
