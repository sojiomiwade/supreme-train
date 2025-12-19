'''
tree122223
{e:2,t:1,r:1,2:4,3:1,1:1}
{4:[2,],2:[e],1:[t,r,]}
now go through the lookup, going down by frequency.
and put freq*each char into an ans list
know the max
ans: []
loop down the frequencies: 4 3 2 1 0

tree
count {t1 r1 e2}
maxf 2
chars {1:[t,r] 2:[e]}
freq 2 [2 .. 1]
ans [eetr]
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        chars=defaultdict(list)
        maxf=max(count.values())
        for ch,chcount in count.items():
            chars[chcount].append(ch)
        ans=[]
        for freq in range(maxf,0,-1):
            for ch in chars[freq]:
                ans.append(ch*freq)
        return ''.join(ans)