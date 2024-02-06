'''
discuss.leetcode.com
discuss  leetcode  com
com leetcode discuss

com.leetcode
[com,leetcode,discuss]
'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dcount=Counter()
        for countplusdomain in cpdomains:
            count,cpdomain=countplusdomain.split()
            cur=[]
            for subdomain in reversed(cpdomain.split('.')):
                cur.append(subdomain)
                dcount[tuple(cur)]+=int(count)
        res=[]
        for rdomain,count in dcount.items():
            res.append(str(count) + ' ' + '.'.join(reversed(rdomain)))
        return res