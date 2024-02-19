'''
create a mapping for each word
abca: abc
cba: abc
...
now loop (i and j) when i and j have same mappings increment count
time,space: O((wn)**2),O(nw)

ab          0
abb         1
abba        2
abbbba      3
.
3+2+1=6     
i :    0
ans :  0 1 3 6 10 
freq : 1 2 3 4
so two things going on: 
    1. can use a 32-bit int to manage the set of chars (which you don't have to do) as set suffices but adds to the space complexity
    2. analytically, everytime you add a new token (that has x others sharing the map
        ), then the answer should increment by the number x (as this new one marries each of the existing x)

so ans is always ans+=count[mapped], and count[mapped] just always increments by 1
'''
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        unique={word:set(word) for word in words}
        n=len(words)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if unique[words[i]]==unique[words[j]]:
                    count+=1
        return count