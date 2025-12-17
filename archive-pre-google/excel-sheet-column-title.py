'''
28 - AB = 1
aa 26+1 27
ac 29
ad 30
...
ab 28

az 26+26
ba 26+26+1 = 2*26 + 1
zy 26*26+25*26^0
bb ba+1
aaa 26+26+1
aab
aaz 26+26+
701 -> ZY
multiply 26 into the 
xay = 25*26**0 + a*26**1 + x*26**2
modulo 28 is 2
then div 26, and you get 1
tag on 1->A 

as long as cn is not 0, the mod digit is the 
    next to add to ans after we convert it to char
then reverse the whole thing

3 % 26 --> 3 - 1 + 97

26%26 --> (0 - 1)%26 + 97 = 

1 + (97-1)
2 + 
...
0+26 + ()
AB -- 28

cn 1
buf [b 97]
mod 2

29 ac
mod -- 3 -- 3 - 1 = 2 = a
29 // 26 == 

26 z
mod -- 0 -- 0 - 1 = -1 = 25 = z 

701
y
701
26

26 // 26 == 1
1 2 3 ... 26
a b c      z
'''
class Solution:
    def convertToTitle(self, cn: int) -> str:
        buf=[]
        alen=26
        while cn>0:
            mod=(cn-1)%alen
            buf.append(chr(65+mod))
            cn=(cn-1)//alen
        return ''.join(reversed(buf))
        