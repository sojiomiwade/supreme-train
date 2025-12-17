'''
increase your score with small tokens
get more power with big tokens

stokens []
power 250
res,cur 1 0
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        stokens=deque(sorted(tokens))
        res=cur=0
        while stokens and (stokens[0]<=power or cur>0):
            if stokens[0]<=power:
                power-=stokens.popleft()
                cur+=1
                res=max(res,cur)
            else:
                power+=stokens.pop()
                cur-=1
        return res

