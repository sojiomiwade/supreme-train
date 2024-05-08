'''
can just call sort on the -ve of the frequency 
t r e e 

e 2, r 1, t 1
1 [r,t]
2 [e]

first get lcount.
then use that to get chars 
time: O(n); space also O(n)
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        lcount=collections.Counter(s)
        # chars=collections.defaultdict(list)
        # for count,let in lcount.items():
        #     chars[count].append(let)
        return ''.join(sorted(s,key=lambda ch: (-lcount[ch],ord(ch))))
