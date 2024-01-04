
def filter_for_sorted(slist: List[str]) -> List[str]:
    res=[]
    for s in slist:
        for i in range(1, len(s)):
            if s[i-1] > s[i]:
                break
        else:
            res.append(s)
    return res

def get_k_len_sorted_strings(k: int) -> List[str]:
    dp=[[] for _ in range(1+k)]
    dp[0]=['']
    for i in range(k + 1):
        for s in dp[i - 1]: # a b
            for ksi in range(26):
                ch=chr(ksi + 97)
                dp[i].append(s+ch)
        dp[i]=filter_for_sorted(dp[i])
    return dp[k]

# print(get_k_len_sorted_strings(2))

ans=get_k_len_sorted_strings(3)
assert len(ans)==len(set(ans))
print(len(ans))
