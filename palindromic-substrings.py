'''
just read out with one char and with two chars
12345654321
     i

  n o o n
        i 
      l
          r
count 6
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(n):
            jl=jr=i
            while jl>=0 and jr<n and s[jl]==s[jr]:
                count+=1
                jl,jr=jl-1,jr+1

        for i in range(n):
            jl,jr=i-1,i
            while jl>=0 and jr<n and s[jl]==s[jr]:
                count+=1
                jl,jr=jl-1,jr+1

        return count