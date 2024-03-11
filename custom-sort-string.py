'''
1. go through order and spit out each element according to count in s, while redcucing count to 0 for each char
2. now spit out remaining characters according to their count
order cba 
s abcd
ans [c b a 1]
count [0 0 0 1 0]

'''
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # below is O(n). now try for sort n lg n
        pos=defaultdict(int)
        for i,ch in enumerate(order):
            pos[ch]=i
        return ''.join(sorted(s,key=lambda ch: pos[ch]))

        # MAXCOUNT=26
        # count=[0 for _ in range(MAXCOUNT)]
        # for ch in s:
        #     count[ord(ch)-ord('a')]+=1
        # ans=[]
        # for ch in order:
        #     ans.extend(count[ord(ch)-ord('a')]*ch)
        #     count[ord(ch)-ord('a')]=0
        # for i in range(26):
        #     ans.extend(count[i]*chr(i+ord('a')))
        # return ''.join(ans)


