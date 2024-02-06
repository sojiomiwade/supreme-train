'''
start a buf: for every word thrown in, add that word.len plus a space to buflen
but if next word will be more than buflen, reset buf and buflen after first
putting buf into res

01234567890123456
012   34   56  78
012 34 56 78 90123          
example  of  text

8 blanks => 17 - 9
8 // (4-1) = 2  => each of the 3 regions gets 2 spaces
8 %  (4-1) = 2 => first 2 regions gets an extra space

if [at the end] wordsbuffer has stuff, then flush it
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordsbuffer, buflen = [], 0
        res = []
        for word in words:
            if len(word) + buflen > maxWidth:
                res.append(wordsbuffer[:])
                wordsbuffer, buflen = [], 0
            buflen += 1 + len(word)
            wordsbuffer.append(word)
        res.append(wordsbuffer[:])
        
        '''
        string=[012,34,56,78],slen=9,wc=4,bc=17-9=8,sp1=8//3=2,sp=8%3=1
            01234567890123456
            '012   34   56  78'
        s2= [012   34   56  78  ]
        string=[012345678], slen=9, wc=1, bc=16-9=7, sp1=7, sp2=0
        string2=[]
        '''
        res2=[]
        for i,string in enumerate(res):
            slen=len(''.join(string))
            word_count=len(string)
            blanks_count=maxWidth-slen
            sp1,sp2=blanks_count,0
            if i==len(res)-1:
                sp1,sp2=1,0
            elif word_count>1:
                sp1=blanks_count//(word_count-1)
                sp2=blanks_count%(word_count-1)
            string2=[]
            for word in string:
                string2.append(word)
                string2.append(' '*sp1)
                string2.append(' '*(sp2>0))
                sp2-=1
            res2.append(''.join(string2)[:maxWidth])
        res2[-1]+=(maxWidth-len(res2[-1])) * ' '
        return res2





        print(res)
        return []