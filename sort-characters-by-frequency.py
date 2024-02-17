'''
assume n is len(s)
can do it in n lg n. 
could also do it in 
manmanm
a2m3n2

could make a list out of above, 
    after creating the hashmap counter
    and sort that and spit out elements by their frequency of those
m3 a2 n2
sort: n + k log k
space: k

finally, after creating hashmap counter, could bucket each char,
    then come from the bottom, spitting out chars by frequency
0
1
2 : a,n
3 : m
mmm + aa + nn
time: n + k
space: k
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        maxf=max(count.values())
        chlookup=defaultdict(list)
        for ch,chcount in count.items():
            chlookup[chcount].append(ch)
        ans=[]
        for freq in range(maxf,0,-1):
            for ch in chlookup[freq]:
                ans.extend(freq*[ch])
        return ''.join(ans)
