'''
leEetcode
 p
   i
p goes back, so the rest of the string is shifted onto it
'''
class Solution:
    def makeGood(self, s: str, p: int = 0) -> str:
        t=[' ']+list(s)
        for i in range(len(t)):
            if abs(ord(t[i])-ord(t[p-1]))==32:
                p-=1
            else:
                t[p]=t[i]
                p+=1

        return ''.join(t[1:p])