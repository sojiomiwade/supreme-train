'''
need to just check if each s char can be found in t
each char checked from s, start from that loc in t

abcde
     t
  s
aec

''
aq
s
t
ahabc

a=[0,4] 
bisect is the one you want, then no need to say idx+1


loc=0
ll[loc] to bisect to get zero

idx=bisect(ll[ch],x=loc,lo=)
t[idx]

loc<-bisect()
we return ll[c][loc] # loc is 0 here
?<-br(ll[c],ll[c][loc]) # loc is 
bisect(idx) cannot be n. if it is return false
ace
binsearch: the whole string starting from last found idx + 1
return False if binsearch cant find

complexity: 
m,n=len(s),len(t)
k is number of s

current approach: k*(m+n)
binsearch: k* m(lg n)
t=abcdacec
  012345678
    l  l l
s=ccc
c=[2,5,7]
2<-0=bisect(loc) #loc is 0
5<-1=bisect(loc) #loc is 2
7<-2=bisect(loc) #loc is 5

'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def lots_of_s():
            m,n=len(s),len(t)
            ll=defaultdict(list)
            for i,x in enumerate(t):
                ll[x].append(i)
            loc=-1
            for x in s:
                idx=bisect.bisect(ll[x],loc)
                if idx==len(ll[x]):
                    return False
                loc=ll[x][idx]
            return True

        def advance_s_conditionally():
            #alternative way - outside idx on t
            if not s:
                return True
            sidx=0
            for tch in t: 
                if tch==s[sidx]:
                    sidx+=1
                if sidx==len(s):
                    return True
            return False

        def find_s_in_t():
            tit=iter(t)
            return all(sch in tit for sch in s)

        return lots_of_s()