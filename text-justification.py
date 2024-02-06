'''
["This", "is", "an", "example", "of", "text", "justification."], 
maxWidth = 16
[
    0123456789012345
    This is an .....
    give each word spaces/word

    20spaces 3words
    55//8 = 6
    55%8 = 7 --extra. give every word 1 from the extra as long as there's extra
    say extra is 5 then 0...4 get an extra => add (idx<extra)
    example of text.
    justification.
    0123456789012345
   "This    is   and", spaces=16-(4+2+3)=7, 7
   (16-3)-(4+2)=13-6=7
   ah wait distribution is actually based on one less word

   "example  of text",
   "justification.  "
]
1. getting the strings: use a buffer, and reset it when string will overflow
2. justification: 
    ignore last line
    spaces=(maxWidth-len(last)) - sum(all words len except last)
    to each words_except_last, pad in front spaces//wordcount + bool(idx<extra)
    'ab cd '
                spaces=(maxWidth-len(last)) - sum(all words len except last)
                to each words_except_last, pad in front spaces//wordcount + bool(idx<extra)
                16-4 - (7-4)
      01234567
["This        is        an","example        of        text","justification.  "]
["This    is    an","example  of text","justification.  "]

012345678901234 = 
aa bb cc d .... = total of 8 spaces
0  1  2  3
wordslist[i%(n-1 or 1)] <-- or 1 in case there's only 1
collect all the spaces
maxWidth-len(letters) <--that's how many we need to distribute
need to do so in front of each word in wordslist
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordslist,letterslen=[],0
        ans=[]
        for word in words:
            if letterslen+len(wordslist)+len(word)>maxWidth:
                for i in range(maxWidth-letterslen):
                    wordslist[i%(len(wordslist)-1 or 1)]+=' '
                ans.append(''.join(wordslist))
                wordslist,letterslen=[],0
            wordslist.append(word)
            letterslen+=len(word)
        return ans+[' '.join(wordslist).ljust(maxWidth)]