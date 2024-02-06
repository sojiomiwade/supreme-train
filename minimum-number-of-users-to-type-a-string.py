'''
find the minimim number of users required to generate a given string s, given that any user can only type a string 'chat'. if no number of users can do this, return -1

chatchat -- ans is 1
chCaHtAT -- ans is 2
chatcCHAhTat -- ans is 2
tahc -- -1, no number of users could do this
ct -- -1, no number of users could do this 

h c   a   t  
    c   h   a t
0 1 2 3 4 5 6 7
-1

c h   a   t  
    c   h   a t
0 1 2 3 4 5 6 7
2

c h t
    c h a t
    0 1 3 2

ccccchhhhh at at at at at 
    c h a t
    8 8 0 0 
    3 3 0 0 
ch ch ch at at at at
look to your left to see if there is a violation

c h a t
0 1 3 5 
2 4 6 7
'''
def count_users(s: str) -> int:
    count=[0 for _ in range(4)]
    ord={ch:i for i,ch in enumerate("chat")}
    INF=float('inf')
    res=-INF
    for ch in s:
        ordch=ord[ch]
        count[ordch]+=1
        if ordch>0 and count[ordch]>count[ordch-1]:
            return -1
        if ordch<3:
            res=max(res,count[ordch]-count[ordch-1])
    assert type(res) is int
    return res
'''
chatchat -- ans is 1
chCaHtAT -- ans is 2
chatcCHAhTat -- ans is 2
tahc -- -1, no number of users could do this
ct -- -1, no number of users could do this 
'''
ss=['chatchat','chCaHtAT','chatcCHAhTat','tahc','ct']
for s in ss: 
    print(f'{s}:{count_users(s.lower())}')