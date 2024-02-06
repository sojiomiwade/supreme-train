'''
cpdomains = [
    "900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

for each dom, split it tokens, then make a deque out of it
for each token
    count[token+rest-of-tokens]+=rep
    tokens.popleft(0)
then output [count key-of-count]
'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count=Counter()
        for cpdomain in cpdomains:
            rep,doms=cpdomain.split()
            irep=int(rep)
            doms_l=cpdomain.split('.')
            if len(doms_l)==3:
                a,b,c=doms_l
                count[doms]+=irep
                count[f'{b}.{c}']+=irep
                count[c]+=irep
            else:
                b,c=doms_l
                count[doms]+=irep
                count[c]+=irep
        return [f'{countval} {irep}' for irep,countval in count.items()]
