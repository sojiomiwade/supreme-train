'''

0123456789
ackn
mw=10
spacecount=10-4 = 6
6//() <-- won't hold if only one string

pack as many as you can to form arr. 
then do lines 2-6 above if len(arr)==1. otherwise do lines 7-11
a 4 b 4 c 3 d 3 e  <-- spacecount=maxwidth-charlen(arr)
= 14 spaces
14/(5-1) = 3
14%(5-1) = 2

mw 16
0123456789012345
This    iss   an  <-- expected ans
words [This iss an]
charlen 9
arr [[This] [iss] [an]]
subans,m [],3
spacecount 16-9 = 7
betcount 7//2 3
extracount 7%2 1
spaces ['    ','   ','']
subans [This4 iss3 an]
this Iss
01234567
4+3+2
'''
class Solution:
    def fullJustify(self, words: List[str], maxwidth: int) -> List[str]:
        arr=[]
        charlen=0
        ans=[]
        for word in words:
            if charlen+len(word)+len(arr)>maxwidth:
                print(arr)
                if len(arr)==1:
                    ans.append(arr[0]+(maxwidth-len(arr[0]))*' ')
                else:
                    m=len(arr)
                    spacecount=maxwidth-charlen
                    betcount=spacecount//(m-1)
                    extracount=spacecount%(m-1)
                    spaces=[' '*betcount]*(m-1)
                    spaces=[spaces[i] + ' '*int(i<extracount)  for i in range(len(spaces))]
                    spaces.append('')
                    assert len(arr)==len(spaces)
                    subans=[word+sp for word,sp in zip(arr,spaces)]
                    ans.append(''.join(subans))
                arr=[word]
                charlen=len(word)
            else:
                arr.append(word)
                charlen+=len(word)
        ans2=''.join(word+' ' for word in arr)
        ans2=ans2[:len(ans2)-1]
        ans3=(maxwidth-len(ans2))*' '
        return ans+[ans2+ans3]
