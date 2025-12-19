'''
900 google.mail.com
domains [mail,com]

count [google.mail.com 900  mail.com 900 ]
'''
class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count=Counter()
        for cpdomain in cpdomains:
            domcount,domain=cpdomain.split()
            domains=deque(domain.split('.'))
            while domains:
                count['.'.join(domains)]+=int(domcount)
                domains.popleft()
        return [f'{domcount} {domain}' for domain,domcount in count.items()]